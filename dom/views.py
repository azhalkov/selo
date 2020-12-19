from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .models import Categori, DomDokument, Adres, Articul
from .forms import CategoriForm, DomDokumentForm, AdresForm, ArtikulForm

# Create your views here.

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