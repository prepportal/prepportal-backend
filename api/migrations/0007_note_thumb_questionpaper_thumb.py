# Generated by Django 4.2.4 on 2023-08-31 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_semester_branch_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='thumb',
            field=models.URLField(default='https://akashrchandran.in'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionpaper',
            name='thumb',
            field=models.URLField(default='https://akashrchandran.in'),
            preserve_default=False,
        ),
    ]