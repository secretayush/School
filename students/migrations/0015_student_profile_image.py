# Generated by Django 2.1 on 2018-08-27 19:09

from django.db import migrations, models

import students.models


class Migration(migrations.Migration):
    dependencies = [
        ('students', '0014_auto_20180825_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to=students.models.user_directory_path),
        ),
    ]