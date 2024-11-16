from django.contrib import admin
from django.urls import path
from agents import views

urlpatterns = [
    path('add/', views.add),
]
