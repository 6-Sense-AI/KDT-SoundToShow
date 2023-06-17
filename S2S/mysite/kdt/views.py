from django.shortcuts import render
from .models import Audio
from . import wav_change_model
import os

def index(request):
    audio = Audio.objects.all()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    print(audio)
    return render(request, 'index.html', {"audio":audio})

def changeAudio(request): # 주파수 변환
    current_directory = os.path.dirname(os.path.abspath(__file__)) # 현재 경로
    wav_change_model.wave_change('success.mp3', 0.6, 25.08, os.path.join(current_directory,'media','origin'),os.path.join(current_directory,'media','change'))
    return render(request, 'audio.html')



# def test(request):
#     wav_change_model('test', 0.6, 25.08, '.', '.')

#     print(audio)
#     return render(request, 'index.html', {"audio":audio})
