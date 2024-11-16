from django.contrib import admin
from django.urls import path
from customers import views

urlpatterns = [
    path('add/', views.add),
    path('get/<int:agent_id>/', views.get)
]
