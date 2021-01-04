from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet, Q
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .models import Categori, DomDokument, Adres, Articul
from .forms import CategoriForm, DomDokumentForm, AdresForm, ArtikulForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
""" Страница приложения дом"""
def index(request):
    return render(request, 'dom/index.html')


"""Форма на сайт модели Articul"""
class ArtikulView(View):
    template_name = 'dom/forms/articul_form.html'
    form_class = ArtikulForm
    model = Articul

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})



class CategoriView(View):
    template_name = 'dom/forms_html/categori_form.html'
    form_class = CategoriForm
    model = Categori

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})


class DomDokumentView(View):
    template_name = 'dom/forms_html/categori_form.html'
    form_class = DomDokumentForm
    model = DomDokument

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})


class AdresView(View):
    """ Класс форма для добавления адреса объекта"""
    template_name = 'dom/forms/adres_form.html'
    form_class = AdresForm
    model = Adres

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})


class AdresListView(ListView):
    template_name = 'dom/pokaz/adres_list.html'
    model = Adres
    context_object_name = 'doma'

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:
            queryset = self.model._default_manager.all()
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                }
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset


class AdresDetailView(DetailView):

    model = Adres
    context_object_name = 'adresa'
    template_name = 'dom/pokaz/adresa_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PoiskAdres(ListView):
    """Класс поиска по артикулу"""
    model = Adres
    template_name = 'dom/search_list.html'


class SearchResultsView(ListView):
    model = Articul
    template_name = 'dom/search_list.html'
    context_object_name = 'artikuli'


    def get_queryset(self):
        query = self.request.GET.get('q')
        artikuli = Articul.objects.filter(region__istartswith=query)
        return artikuli

