from sys import _enablelegacywindowsfsencoding
from django.shortcuts import render
from .models import Restaurants, Codes, Clients, TextAccueil, TextLeConcours
from . import forms
import folium
from random import randint
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):

    text_accueil = TextAccueil.objects.first()

    context = {
        'text_accueil':text_accueil,
    }

    return render(request, 'index.html', context)

def concours(request):

    text_concours = TextLeConcours.objects.first()

    items_list = []

    item_1 = text_concours.text_p_2_item_1
    if item_1 != None:
        items_list.append(item_1)
    item_2 = text_concours.text_p_2_item_2
    if item_2 != None:
        items_list.append(item_2)
    item_3 = text_concours.text_p_2_item_3
    if item_3 != None:
        items_list.append(item_3)
    item_4 = text_concours.text_p_2_item_4
    if item_4 != None:
        items_list.append(item_4)
    item_5 = text_concours.text_p_2_item_5
    if item_5 != None:
        items_list.append(item_5)
    item_6 = text_concours.text_p_2_item_6
    if item_6 != None:
        items_list.append(item_6)

    context = {
        'text_concours':text_concours,
        'items_list': items_list, 
    }

    return render(request, 'concours.html', context)


def votation(request):
    
    error = ""
    form = forms.VotationForm()

    if request.method == "POST":

        form = forms.VotationForm(request.POST)
        restaurants = Restaurants.objects.all()

        if form.is_valid():

            for restaurant in restaurants:

                codes = Codes.objects.filter(restaurant_name = restaurant.restaurant_name)

                if codes.exists():
                    
                    form_code = int(form.data['code'])
                    form_note = int(form.data['note'])
                    
                    for code in codes:
                        if (code.value == form_code) and (form_note in range(0,101) and (code.status=="disponible")) :

                            print("le code correspond")
                            
                            restaurant.note_moyenne = (restaurant.note_moyenne*restaurant.nb_votes + form_note)/(restaurant.nb_votes+1)
                            restaurant.nb_votes = restaurant.nb_votes + 1
                            code.status = "indisponible"

                            restaurant.save()
                            code.save()
                            
                            return HttpResponseRedirect('/votation/thanks')

                        elif (code.value == form_code) and (code.status=="indisponible"):
                            error = "Le code a deja ete utilise, veuillez en renseigner un autre"
                            return render(request, 'votation.html', {'form': form, 'error':error})

                        else:
                            error = "Le code ou la note ne sont pas correctements renseignes"

                # creer 200 codes pour le restaurant de 8 digits differents
                else:
                    for x in range( 200 ):
                        Codes.objects.create(restaurant_name=restaurant.restaurant_name,
                                         value=randint(10000000, 99999999),
                                         status="disponible")


    return render(request, 'votation.html', {'form': form, 'error':error})


def votation_done(request):

    return render(request, 'votation_done.html')


def restaurant_page(request,restaurant_name):
    restaurant = Restaurants.objects.get(restaurant_name=restaurant_name)
    return render(request, "restaurant_page.html", {"restaurant":restaurant})

def restaurants(request):

    m = folium.Map(location=[46.203561251367034, 6.145632067729674], zoom_start=14, max_bounds=True, min_zoom=12, max_zoom=18, 
                            max_lat=46.32536087168599, min_lat=46.115976770540996, min_lon=5.9096901580846986, max_lon=6.332353664526888,
                            tiles=None)
    
    folium.TileLayer('openstreetmap',attr=None, opacity=0.7, min_zoom=12).add_to(m)



    restaurants= Restaurants.objects.all()

    add_restaurants_to_map(m,restaurants)

    m = m._repr_html_()

    context = {
        'm':m,
        'restaurants':restaurants,
    }

    return render(request, 'restaurants.html', context)


def add_restaurants_to_map(m, restaurants):

    for restaurant in restaurants:
        print(restaurant.restaurant_name)
        href_balise =  "<a href=/restaurants/"+restaurant.restaurant_name+">voir la page"+"</a>"
        print(href_balise)
        iframe = folium.IFrame('<strong>Restaurant : </strong>' + restaurant.restaurant_name + '<br>' + href_balise)
        popup = folium.Popup(iframe, min_width=300, max_width=300)
        folium.Marker([restaurant.loc_lat, restaurant.loc_lon], popup=popup, tooltip='voir le restautrant').add_to(m)

    return


def connexion(request):

    form = forms.InscriptionForm()
    error = ""

    if request.method == "POST":

        form = forms.InscriptionForm(request.POST)
        #clients = Clients.objects.all()
        if form.is_valid():

            form_nom = form.data['nom']
            form_prenom = form.data['prenom']
            form_adresse = form.data['adresse']
            form_NPA = form.data['NPA']
            form_ville = form.data['ville']
            form_pays = form.data['pays']

            form_adresse_mail = form.data['adresse_mail']
            form_password = form.data['password']

            if form_adresse_mail == "gkathari@gmail.com":
                error = "Cette adresse mail est deja utilisee"

            elif "@" not in form_adresse_mail:
                error = "L'adresse mail est incorrecte"
            else:
                print("adresse mail valide")
            

    context = {
        'form':form,
        'error':error
    }

    return render(request, 'connexion.html', context)

