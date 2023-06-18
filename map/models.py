from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models


class TextAccueil(models.Model):

    text_date = models.CharField(max_length=200)

    text_p_1_1 = models.CharField(max_length=2000, blank=True, null=True)
    text_p_1_2 = models.CharField(max_length=2000, blank=True, null=True)
    text_p_1_3 = models.CharField(max_length=2000, blank=True, null=True)

    text_p_2_1 = models.CharField(max_length=2000, blank=True, null=True)
    text_p_2_2 = models.CharField(max_length=2000, blank=True, null=True)
    text_p_2_3 = models.CharField(max_length=2000, blank=True, null=True)

    text_p_3_1 = models.CharField(max_length=2000, blank=True, null=True)
    text_p_3_2 = models.CharField(max_length=2000, blank=True, null=True)
    text_p_3_3 = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.text_date
    

class TextLeConcours(models.Model):


    text_p_1_1 = models.CharField(max_length=2000, blank=True, null=True)
    text_p_1_2 = models.CharField(max_length=2000, blank=True, null=True)
    text_p_1_3 = models.CharField(max_length=2000, blank=True, null=True)

    text_p_2_1 = models.CharField(max_length=2000, blank=True, null=True)
    text_p_2_2 = models.CharField(max_length=2000, blank=True, null=True)

    text_p_2_item_1 = models.CharField(max_length=2000, blank=True, null=True)
    text_p_2_item_2 = models.CharField(max_length=2000, blank=True, null=True)
    text_p_2_item_3 = models.CharField(max_length=2000, blank=True, null=True)
    text_p_2_item_4 = models.CharField(max_length=2000, blank=True, null=True)
    text_p_2_item_5 = models.CharField(max_length=2000, blank=True, null=True)
    text_p_2_item_6 = models.CharField(max_length=2000, blank=True, null=True)

    text_p_2_3 = models.CharField(max_length=2000, blank=True, null=True)
    text_p_2_4 = models.CharField(max_length=2000, blank=True, null=True)

    text_p_3_1 = models.CharField(max_length=2000, blank=True, null=True)
    text_p_3_2 = models.CharField(max_length=2000, blank=True, null=True)
    text_p_3_3 = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.text_p_1_1


# Create your models here.

class Restaurants(models.Model):

    restaurant_name = models.CharField(max_length=200)
    restaurant_description = models.TextField(max_length=1000)
    restaurant_adresse = models.CharField(max_length=500, blank=True, null=True)
    restaurant_site = models.CharField(max_length=200, blank=True, null=True)

    burger_name = models.CharField(max_length=200)
    burger_description = models.TextField(max_length=1000)

    restaurant_logo = models.ImageField(blank=True, null=True,upload_to="media")
    burger_image = models.ImageField(blank=True, null=True,upload_to="media")

    nb_votes = models.IntegerField(default=0)
    note_moyenne = models.FloatField(default=0)

    loc_lon = models.CharField(max_length=200)
    loc_lat = models.CharField(max_length=200)

    def __str__(self):
        return self.restaurant_name

class Codes(models.Model):

    restaurant_name = models.CharField(max_length=200)
    value = models.IntegerField()

    status = models.CharField(max_length=100, default="disponible")

    def __str__(self):
        return str(self.value)

class Clients(models.Model):

    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    NPA = models.IntegerField()
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=200)

    adresse_mail = models.CharField(max_length=200)
    password = models.CharField(max_length=20)


    def __str__(self):
        return self.adresse_mail

