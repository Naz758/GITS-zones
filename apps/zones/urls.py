from django.urls import path

from . import views

app_name = "zones"

urlpatterns = [
    path("", views.ZoneListView.as_view(), name="zone-list-view"),
    path("create-zone", views.ZoneCreateView.as_view(), name="zone-create-view"),
    path("<int:pk>", views.ZoneDetailView.as_view(), name="zone-detail-view"),
    path("profile/<int:pk>", views.ProfileUpdateView.as_view(), name="profile-detail-view"),
    path("techs", views.ProfileListView.as_view(), name="tech-list-view"),
    path("agency/<int:pk>", views.AgencyDetailView.as_view(), name="agency-detail-view"),

]
