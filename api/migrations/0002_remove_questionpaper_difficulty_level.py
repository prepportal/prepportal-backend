# Generated by Django 4.0.3 on 2023-08-27 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionpaper',
            name='difficulty_level',
        ),
    ]