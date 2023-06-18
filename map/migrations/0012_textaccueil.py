# Generated by Django 4.1.1 on 2023-06-09 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0011_restaurants_restaurant_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextAccueil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_date', models.CharField(max_length=200)),
                ('text_p_1_1', models.CharField(blank=True, max_length=2000, null=True)),
                ('text_p_1_2', models.CharField(blank=True, max_length=2000, null=True)),
                ('text_p_1_3', models.CharField(blank=True, max_length=2000, null=True)),
                ('text_p_2_1', models.CharField(blank=True, max_length=2000, null=True)),
                ('text_p_2_2', models.CharField(blank=True, max_length=2000, null=True)),
                ('text_p_2_3', models.CharField(blank=True, max_length=2000, null=True)),
                ('text_p_3_1', models.CharField(blank=True, max_length=2000, null=True)),
                ('text_p_3_2', models.CharField(blank=True, max_length=2000, null=True)),
                ('text_p_3_3', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]
