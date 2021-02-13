from itertools import chain
from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet, Q
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.views import View
from .models import Categori, DomDokument, Adres, Articul, Person, FotoDom
from .forms import CategoriForm, DomDokumentForm, AdresForm, ArtikulForm, PersonForm, FotoDomForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

'''https://www.youtube.com/watch?v=v2L3oyO8SX8  '''

def index(request):
    """ Страница приложения дом"""
    return render(request, 'dom/index.html')


class ArtikulView(View):
    """Форма на сайт модели Articul"""
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
    """Форма на сайт модели Categori"""
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


class PersonView(View):
    """Форма на сайт модели Person"""
    template_name = 'dom/forms_html/person_form.html'
    form_class = PersonForm
    model = Person

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})


class FotoDomView(View):
    """Форма на сайт модели FotoDom"""
    template_name = 'dom/forms/foto_dom_form.html'
    form_class = FotoDomForm
    model = FotoDom

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
    context_object_name = 'da'


    def get_queryset(self):
        query = self.request.GET.get('q')
        if query == None:
            query = '123'
        artikuli = Articul.objects.filter(region__istartswith=query)
        return artikuli



""" Поиск по несольким моделям"""

def dom_poisk(request, ):
    query = request.GET.get('q')
    if query == None:
        query = 'Поиск'
    articuli = Articul.objects.filter(region__istartswith=query)
    # articuli = Articul.objects.all()
    adres = Adres.objects.filter(gorod__istartswith=query)
    foto = FotoDom.objects.all()
    context = {'articuli': articuli, 'adres': adres, 'foto': foto}
    return render(request, 'dom/poisk/dom_poisk_list.html', context)



class PoiskDomView(ListView):
    model = Articul
    template_name = 'dom/poisk/dom_poisk_list.html'
    context_object_name = 'ok'


    def get_queryset(self):
        query = self.request.GET.get('q')
        if query == None:
            query=''

        object_list = Articul.objects.filter(Q(art__icontains=query) | Q(kod_phone__icontains=query) )
        # object_list = object_list.filter(is_activ=True) # Фильтр по полю is_activ
        return object_list





class ArticulDetailView(DetailView):
    model = Articul
    template_name = 'dom/poisk/dom_poisk_detail.html'
    queryset = Articul.objects.all()
    context_object_name = 'ok' # имя модели для html шаблона

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context


class SearchDetailView(DetailView):
    model = Articul
    template_name = 'dom/dom_search_detail.html'
    queryset = Articul.objects.all()
    # slug_field = 'url'
    context_object_name = 'da'  # имя модели для html шаблона



