from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("quote/", views.contact, name="contact"),
    path("privacy/", views.privacy, name="privacy"),
    path("projects/", views.projects, name="projects"),
    path("services/", views.services_index, name="services_index"),
    path("services/<slug:slug>/", views.service_detail, name="service_detail"),
    path("robots.txt", views.robots_txt, name="robots_txt"),
]
