from django.shortcuts import render
from .models import Audio

def index(request):
    audio = Audio.objects.all()
    print(audio)
    return render(request, 'index.html', {"audio":audio})
