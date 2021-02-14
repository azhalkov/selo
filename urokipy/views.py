""" urokipy/views """
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic import ListView
from . models import Karta


class KartaListView(ListView):
    template = 'urokipy/stroki.html'
    model = Karta
    context_object_name = 'kartochki'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context