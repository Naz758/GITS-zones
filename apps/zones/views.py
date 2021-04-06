from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from .models import Agency, Zone


class ZoneCreateView(CreateView):
    model = Zone
    fields = ["name"]


class ZoneListView(ListView):
    model = Zone


class ZoneDetailView(DetailView):
    model = Zone
