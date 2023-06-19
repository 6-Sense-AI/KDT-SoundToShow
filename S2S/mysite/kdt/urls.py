from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'kdt'
urlpatterns = [
    path('', views.index, name='index'),
    path('audio', views.changeAudio, name='audio'),
    path('upload', views.videoUpload, name='upload'),
]