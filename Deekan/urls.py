from django.contrib import admin
from django.urls import path
from Deekan import views

urlpatterns =[
    path("", views.index, name="Deekan"),
    path("About", views.About, name="About"),
    path("Courses", views.Courses, name="Courses"),
    path("Contact", views.Contact, name="Contact"),
]