from django.shortcuts import render
from django.views.generic import ListView

from partner.models import Usluga


class UslugaListView(ListView):
    template_name = 'partner/uslugi.html'
    model = Usluga

