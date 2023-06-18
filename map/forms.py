from django import forms
from django.core.exceptions import ValidationError

def validate_email(value):
    if "@" not in value:
        raise ValidationError("L'adresse email n'est pas valide")

class VotationForm(forms.Form):

    code = forms.IntegerField(widget=forms.TextInput(attrs={'size': 20, 'title': 'Code','placeholder':" 8 chiffres",}))
    #note = forms.IntegerField(widget=forms.TextInput(attrs={'size': 20, 'title': 'Note','placeholder':" de 0 a 100",}))
    note = forms.IntegerField(
    widget=forms.NumberInput(
        attrs={
            'type': 'range',
            'min': 0,
            'max': 100,
            'step': 1,
            'class': 'custom-range'
        }
    )
)

class InscriptionForm(forms.Form):
    nom = forms.CharField(widget=forms.TextInput(attrs={'size': 40,'title': 'Nom','placeholder':"",}))
    prenom = forms.CharField(widget=forms.TextInput(attrs={'size': 40, 'title': 'Prenom','placeholder':"",}))
    adresse = forms.CharField(widget=forms.TextInput(attrs={'size': 40, 'title': 'Adresse','placeholder':"",}))
    NPA = forms.IntegerField(widget=forms.TextInput(attrs={'size': 8, 'title': 'NPA','placeholder':"",}))
    ville = forms.CharField(widget=forms.TextInput(attrs={'size': 40, 'title': 'Ville','placeholder':"",}))
    pays = forms.CharField(widget=forms.TextInput(attrs={'size': 40, 'title': 'Pays','placeholder':"",}))

    adresse_mail = forms.CharField(widget=forms.TextInput(attrs={'size': 40, 'title': 'Adresse mail','placeholder':"",}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'size': 40, 'title': 'Mot de passe','placeholder':"",}))

    accept_terms = forms.BooleanField(label='Accepter les conditions d\'utilisation')




    


    