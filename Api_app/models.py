from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File

# Create your models here.
# Model for creating api for ai tools

class Mainai(models.Model):

    VERSION_CHOICES = [
        ('FR', 'Free'),
        ('PA', 'Paid'),
        ('FM', 'Freemium'),
    ]
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Tagline = models.CharField(max_length=300)
    #field for link
    link = models.URLField(max_length=1000)
    Image = models.ImageField(upload_to='images/')
    version = models.CharField(
        max_length=2,
        choices=VERSION_CHOICES,
        default='FR',
    )

    #todo: field for dynamic page
    Views = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    Description1 = models.TextField(max_length=1000)
    Description2 = models.TextField(max_length=1000)
    keywords = models.CharField(max_length=1000,default='')

    def __str__(self):
        return self.Title + ' - ' + self.Tagline
    
    def save(self, *args, **kwargs):
        if self.Image:
            image = Image.open(self.Image)
            (width, height) = image.size
            "Max width and height 800"
            if width > 800:
                factor = 800.0 / width
                size = (800, int(height * factor))
                image = image.resize(size, Image.LANCZOS)
            if image.mode in ('RGBA', 'LA'):
                image = image.convert('RGB')
            temp_thumb = BytesIO()
            image.save(temp_thumb, format='JPEG')
            temp_thumb.seek(0)

            self.Image = File(temp_thumb, name=self.Image.name)

        super(Mainai, self).save(*args, **kwargs)

    def get_keywords_list(self):
        return [keyword.strip() for keyword in self.keywords.split(',')]
