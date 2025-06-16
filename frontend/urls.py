from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.blog, name="blog"),
    path("friends/", views.friends, name="friends"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]