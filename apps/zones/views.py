from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Agency, Profile, Role, Zone


class ZoneCreateView(CreateView):
    model = Zone
    fields = ["name"]


class ZoneListView(ListView):
    model = Zone


class ZoneDetailView(DetailView):
    model = Zone


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["first_name", "last_name", "email", "ext"]


class ProfileListView(ListView):
    model = Profile


class AgencyDetailView(DetailView):
    model = Agency
