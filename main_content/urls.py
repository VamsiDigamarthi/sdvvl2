from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("highlights/", views.highlights, name="highlights"),
]