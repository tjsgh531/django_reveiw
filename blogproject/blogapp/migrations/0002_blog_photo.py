# Generated by Django 4.1 on 2022-08-10 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='blog_photo'),
        ),
    ]
