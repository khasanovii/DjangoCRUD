# socks/urls.py
from django.urls import path
# now import the views.py file into this code

from . import views

urlpatterns = [
    path('', views.index),
    path('create/',views.create_view, name='create_view')
] 
