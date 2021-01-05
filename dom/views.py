from itertools import chain
from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet, Q
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.views import View
from .models import Categori, DomDokument, Adres, Articul, Person
from .forms import CategoriForm, DomDokumentForm, AdresForm, ArtikulForm, PersonForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


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



""" Поиск по несольким моделям"""
# class SearchResultsView(View):
#     template_name = 'dom/search_list.html'
#
#     def get(self, request, *args, **kwargs):
#         context = {}
#
#         q = request.GET.get('q')
#         if q:
#             query_sets = []  # Общий QuerySet
#
#             # Ищем по всем моделям
#             query_sets.append(Adres.objects.search(query=q))
#             query_sets.append(Articul.objects.search(query=q))
#             query_sets.append(Categori.objects.search(query=q))
#             query_sets.append(Person.objects.search(query=q))
#             query_sets.append(DomDokument.objects.search(query=q))
#
#             # и объединяем выдачу
#             final_set = list(chain(*query_sets))
#             final_set.sort(key=lambda x: x.pub_date, reverse=True)  # Выполняем сортировку
#
#             context['last_question'] = '?q=%s' % q
#
#             current_page = Paginator(final_set, 10)
#
#             page = request.GET.get('page')
#             try:
#                 context['object_list'] = current_page.page(page)
#             except PageNotAnInteger:
#                 context['object_list'] = current_page.page(1)
#             except EmptyPage:
#                 context['object_list'] = current_page.page(current_page.num_pages)
#
#         return render(request=request, template_name=self.template_name, context=context)
