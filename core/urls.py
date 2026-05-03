from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("quote/", views.contact, name="contact"),
    path("privacy/", views.privacy, name="privacy"),
    path("projects/", views.projects, name="projects"),
]
