"""festivalchef URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from map import views as map_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',map_views.index, name='index'),
    path('restaurants/',map_views.restaurants, name='restaurants'),
    path('concours/',map_views.concours, name='concours'),
    path('votation/',map_views.votation, name='votation'),
    path('restaurants/<str:restaurant_name>',map_views.restaurant_page, name='restaurant_page'),
    path('votation/thanks/',map_views.votation_done, name='votation_done'),
    path('connexion/',map_views.connexion, name='connexion')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
