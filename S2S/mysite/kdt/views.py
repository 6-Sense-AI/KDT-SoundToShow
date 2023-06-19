from django.shortcuts import render
from .models import Audio
from . import wav_change_model
from django.core.files.storage import FileSystemStorage
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

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        return render(request, 'upload.html', {
            'message': '파일이 성공적으로 업로드되었습니다.'
        })
    return render(request, 'upload.html')
