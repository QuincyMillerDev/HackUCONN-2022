from django.urls import path
from . import views

urlpatterns = [
    path('', views.question, name='question'), 
    path('question', views.question, name='question')
]