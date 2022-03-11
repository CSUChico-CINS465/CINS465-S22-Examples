# Generated by Django 4.0.2 on 2022-03-10 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_commentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestionmodel',
            name='image',
            field=models.ImageField(max_length=144, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='suggestionmodel',
            name='image_description',
            field=models.CharField(max_length=240, null=True),
        ),
    ]
