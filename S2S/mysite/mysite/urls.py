from django.contrib import admin
from django.urls import path, include
from kdt import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    # path('upload', views.upload),
    path('kdt/',include('kdt.urls')),
]