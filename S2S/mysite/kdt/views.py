from django.shortcuts import render
from .models import Audio
from . import wav_change_model
from django.core.files.storage import FileSystemStorage
import os
from django.http import HttpResponse ,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View

current_directory = os.path.dirname(os.path.abspath(__file__))

def index(request):
    audio = Audio.objects.all()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    print(audio)
    return render(request, 'index.html', {"audio":audio})

def changeaudio(filename, selected_frequency):
    if selected_frequency:
            origin_path = os.path.join(current_directory, 'media', 'sound', 'origin')
            change_path = os.path.join(current_directory, 'media', 'sound','change')
            
            if selected_frequency == '1':   # 저주파 :20 ~ 1000
                wav_change_model.wave_change(filename, "c"+filename, 0.3, 15, origin_path, change_path)
            elif selected_frequency == '2': # 저주파 :20 ~ 2000
                wav_change_model.wave_change(filename, "c"+filename, 0.3, 25.08, origin_path, change_path)
            elif selected_frequency == '3': # 중음역 :500 ~ 3000
                wav_change_model.wave_change(filename, "c"+filename, 7.5, 31, origin_path, change_path)
            elif selected_frequency == '4': # 고주파 :1000 ~ 20000
                wav_change_model.wave_change(filename, "c"+filename, 15, 58.57, origin_path, change_path)
            elif selected_frequency == '5': # 고주파 :2000 ~ 20000
                wav_change_model.wave_change(filename, "c"+filename, 25.08, 58.57, origin_path, change_path)
    return 1

# 파일 업로드
@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage(os.path.join(current_directory,'media','sound','origin')) # 원본 저장

        # 주파수 저장
        audio_id = Audio.objects.latest('id').id + 1 if Audio.objects.exists() else 1 # id 얻기
        filename = f"{audio_id}_{uploaded_file.name}" # 오디오 파일 이름
        fs.save(filename, uploaded_file)
        audio = Audio(id=audio_id, path=fs.path(filename)) #모델에 저장
        audio.save()

        # 주파수 모드
        num = request.POST.get('num')
        print(num)
        print(changeaudio(filename,num)) # 파일 생성
        
        # 입모양 생성 여부
        generate_mouth = request.POST.get('generate_mouth')
        print(generate_mouth)
        
        # 텍스트 생성 여부
        generate_text = request.POST.get('generate_text')
        print(generate_text)

        # 파일 확장자 설정
        if generate_mouth == 'yes' or generate_text == 'yes':
            file_extension = 'mp4'
        else:
            file_extension = 'mp3'

        context = {
            'num': num,
            'generate_mouth': generate_mouth,
            'generate_text': generate_text,
        }

        message = '파일이 성공적으로 업로드되었습니다.'
        return render(request, 'model_result.html', context)
    return render(request, 'upload_file.html')

