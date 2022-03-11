from django.contrib import admin
from django.urls import path, include
from . import views




urlpatterns = [
    path('', views.index),
    path('login/', views.loginPage),
    path('logout/', views.logoutPage),
    path('home/', views.home),
    path('register/', views.registration),
    path('myorder/', views.myorder),
    path('sustainable/', views.sustainable),
    path('contactus/', views.contactus),
    path('distribution/',views.distribution)
]