from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'kdt'
urlpatterns = [
    path('', views.index, name='index'),
    path('uploadfile/', views.upload_file, name='uploadfile'),
]