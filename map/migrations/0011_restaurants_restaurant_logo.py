# Generated by Django 4.1.1 on 2023-05-19 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0010_clients'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='restaurant_logo',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]