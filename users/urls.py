from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
]
