# Generated by Django 4.0.5 on 2022-06-25 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
