from django import forms
from .models import *


class ArtikulForm(forms.ModelForm):
    class Meta:
        model = Articul
        exclude = ['art', 'nomer', 'slug']


class CategoriForm(forms.ModelForm):
    class Meta:
        model = Categori
        exclude = ['objects', 'slug']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['objects', ]


class DomDokumentForm(forms.ModelForm):
    class Meta:
        model = DomDokument
        exclude = ['datepub', 'slug']


class AdresForm(forms.ModelForm):
    class Meta:
        model = Adres
        exclude = ['is_prodaju', 'is_activ', 'is_prodano', 'is_arenda', 'slug' ]
        ordering = "-arti_dokument"


