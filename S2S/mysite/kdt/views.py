from django.shortcuts import render
from .models import Audio
from .wav_change_model import wave_change

def index(request):
    audio = Audio.objects.all()
    wave_change('test.mp3', 0.6, 25.08, 'C:/hackathon/mysite/KDT-SoundToShow/S2S/mysite/kdt/test/input', 'C:/hackathon/mysite/KDT-SoundToShow/S2S/mysite/kdt/test/output')
    print(audio)
    return render(request, 'index.html', {"audio":audio})

