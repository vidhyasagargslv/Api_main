# Generated by Django 5.0.3 on 2024-03-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_app', '0004_mainai_additional_mainai_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainai',
            name='additional',
            field=models.TextField(default='default_category', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mainai',
            name='category',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
