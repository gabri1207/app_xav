# Generated by Django 4.1.1 on 2022-10-09 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_rename_restaurant_restaurants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='burger_image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]