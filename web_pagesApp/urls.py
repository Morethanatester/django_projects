from django.urls import path
from web_pagesApp import views

urlpatterns = [
    path("", views.home, name='home'),
]