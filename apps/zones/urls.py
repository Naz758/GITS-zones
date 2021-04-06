from django.urls import path

from . import views

app_name = "zones"

urlpatterns = [
    path("", views.ZoneListView.as_view(), name="zone-list-view"),
    path("create-zone", views.ZoneCreateView.as_view(), name="zone-create-view"),
    path("<int:pk>", views.ZoneDetailView.as_view(), name="zone-detail-view"),
]
