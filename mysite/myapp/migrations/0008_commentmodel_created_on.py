# Generated by Django 4.0.2 on 2022-03-22 21:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_suggestionmodel_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
