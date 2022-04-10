from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.question, name='question'), 
    path('question', views.question, name='question'),
    path('tell-more', views.tellMore, name='tell-more'),
    path('dashboard', views.dashboard, name='dashboard')
]