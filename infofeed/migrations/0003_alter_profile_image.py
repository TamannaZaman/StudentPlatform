# Generated by Django 3.2.7 on 2021-11-06 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infofeed', '0002_comments_like_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media\\profile_pics\\default.png', upload_to='profile_pics'),
        ),
    ]
