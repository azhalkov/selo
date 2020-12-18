from django import forms
from .models import *


class CategoriForm(forms.ModelForm):
    class Meta:
        model = Categori
        exclude = ['objects', 'slug']


class DomDokumentForm(forms.ModelForm):
    class Meta:
        model = DomDokument
        exclude = ['datepub', 'slug']
