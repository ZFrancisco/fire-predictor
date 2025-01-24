from django.contrib import admin
from django.urls import include, path
from backendHandle import views

urlpatterns = [
    path('', views.index, name="index")
]
