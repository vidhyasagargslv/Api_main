from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File

# Create your models here.
# Model for creating api for ai tools

class Mainai(models.Model):
    """
    Represents a mainai object in Django.

    Fields:
    - id (AutoField): Auto-generated primary key for the mainai object.
    - Title (CharField): Stores the title of the mainai.
    - Tagline (CharField): Stores the tagline of the mainai.
    - link (URLField): Stores the link of the mainai.
    - Image (ImageField): Stores the image of the mainai.
    - version (CharField): Stores the version of the mainai. Choices are 'Free', 'Paid', and 'Freemium'.
    - Views (IntegerField): Stores the number of views of the mainai.
    - rating (IntegerField): Stores the rating of the mainai.
    - Description1 (TextField): Stores the first description of the mainai.
    - Description2 (TextField): Stores the second description of the mainai.
    - keywords (CharField): Stores the keywords of the mainai.

    Methods:
    - __str__(): Returns a string representation of the mainai object, combining the title and tagline.
    - save(): Overrides the default save method to resize and convert the image to JPEG format before saving.
    - get_keywords_list(): Returns a list of keywords by splitting the keywords string.
    """

    VERSION_CHOICES = [
        ('Free', 'Free'),
        ('Paid', 'Paid'),
        ('Freemium', 'Freemium'),
    ]
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Tagline = models.CharField(max_length=300)
    link = models.URLField(max_length=1000)
    Image = models.ImageField(upload_to='images/')
    version = models.CharField(
        max_length=8,
        choices=VERSION_CHOICES,
        default='FR',
    )
    Views = models.IntegerField(default=0)
    rating = models.IntegerField(max_length=1, default=0)
    Description1 = models.TextField(max_length=1000)
    Description2 = models.TextField(max_length=1000)
    keywords = models.CharField(max_length=1000, default='')

    def __str__(self):
        """
        Returns a string representation of the mainai object, combining the title and tagline.
        """
        return self.Title + ' - ' + self.Tagline

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to resize and convert the image to JPEG format before saving.
        """
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
        """
        Returns a list of keywords by splitting the keywords string.
        """
        return [keyword.strip() for keyword in self.keywords.split(',')]



#! documnet for all model
#?id: Auto-generated primary key for the mainai object.
#?Title: CharField to store the title of the mainai.
#?Tagline: CharField to store the tagline of the mainai.
#?link: URLField to store the link of the mainai.
#?Image: ImageField to store the image of the mainai.
#?version: CharField with choices to store the version of the mainai.
#?Views: IntegerField to store the number of views of the mainai.
#?rating: IntegerField to store the rating of the mainai.
#?Description1: TextField to store the first description of the mainai.
#?Description2: TextField to store the second description of the mainai.
#?keywords: CharField to store the keywords of the mainai.
    