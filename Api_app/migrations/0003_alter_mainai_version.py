# Generated by Django 5.0.3 on 2024-03-05 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_app', '0002_mainai_keywords_mainai_version_alter_mainai_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainai',
            name='version',
            field=models.CharField(choices=[('Free', 'Free'), ('Paid', 'Paid'), ('Freemium', 'Freemium')], default='FR', max_length=8),
        ),
    ]
