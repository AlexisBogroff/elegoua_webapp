from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('form/', views.formpage, name='form'),
    path('contact/', views.contactpage, name='contact'),
    path('thanks/', views.thankspage, name='thanks'),
]
