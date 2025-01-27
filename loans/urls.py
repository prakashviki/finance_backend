
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
   
    path('add/', views.add ),
    path('loan_details/<int:loan_id>/', views.loan_details )
]
