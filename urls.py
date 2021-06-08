from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='form'),
    path('sign/', views.sign, name='sign'),
    path('two/', views.two, name='two'),
    path('random/', views.random, name='random'),
    path('random1', views.random1, name='random1'),
]