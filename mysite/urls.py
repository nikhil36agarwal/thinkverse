from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="homepage"),
    path('bbcnews/', views.page2, name = "bbc_news"),
    path('germanybusiness/', views.page3, name = "de_business"),
    path('trumpheadlines/', views.page4, name = "trump_headlines"),
]