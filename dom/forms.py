from django import forms
from .models import *



'''класс Form будет иметь поле формы для каждого указанного поля модели
 в порядке, указанном в атрибуте fields'''
class ArtikulForm(forms.ModelForm):
    class Meta:
        model = Articul
        exclude = ['art', 'nomer', 'slug']


class CategoriForm(forms.ModelForm):
    """Поля формы можно поставить куда захочешь"""
    name = forms.CharField(label="Категория")
    description = models.TextField("Описание")
    slug = forms.URLField(label='Ссылка', required=False)
    objects = False

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


