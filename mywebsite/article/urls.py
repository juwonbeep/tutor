from django.urls import path
from . import views

urlpatterns =  [
    path ('articlereg/', views.articlereg),
    path ('subject/', views.subject),
]