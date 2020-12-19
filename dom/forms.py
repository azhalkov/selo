from django import forms
from .models import *


class ArtikulForm(forms.ModelForm):
    class Meta:
        model = Articul
        exclude = ['']


class CategoriForm(forms.ModelForm):
    class Meta:
        model = Categori
        exclude = ['objects', 'slug']


class DomDokumentForm(forms.ModelForm):
    class Meta:
        model = DomDokument
        exclude = ['datepub', 'slug']


class AdresForm(forms.ModelForm):
    class Meta:
        model = Adres
        exclude = ['is_prodaju', ]


