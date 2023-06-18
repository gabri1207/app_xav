from django.contrib import admin

# Register your models here.
from .models import Restaurants, Codes, TextAccueil, TextLeConcours

admin.site.register(Restaurants)
admin.site.register(Codes)
admin.site.register(TextAccueil)
admin.site.register(TextLeConcours)