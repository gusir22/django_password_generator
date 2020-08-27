'''Defines URL patterns for generator'''

from django.urls import path
from . import views

app_name = 'generator'
urlpatterns = [
    #Home Page
    path('', views.home, name='home'),
    #Generated Password Page
    path('generatedpassword/', views.password, name='password'),
    #About Page
    path('about/', views.about, name='about'),
]