from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("highlights/", views.highlights, name="highlights"),
    path("contact/", views.contact, name="contact"),
    path("projects/", views.projects, name="projects"), 
    path("dashboard/", views.dashboards, name="dashboard"),
    path("blog/", views.blog, name="blog"),
    
]