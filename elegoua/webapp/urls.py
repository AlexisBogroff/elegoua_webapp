from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('form/', views.formpage, name='form'),
    path('origins/', views.originpage, name='origins'),
    path('team/', views.teampage, name='team'),
    path('contact/', views.contactpage, name='contact'),
    path('demo/', views.demopage, name='demo'),
    path('thanks/', views.thankspage, name='thanks'),
]
