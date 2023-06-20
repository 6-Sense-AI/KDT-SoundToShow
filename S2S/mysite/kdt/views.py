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

def uploadFile(request):
    return render(request,'upload_file.html')

# def changeAudio(request): # 주파수 변환
#     current_directory = os.path.dirname(os.path.abspath(__file__)) # 현재 경로
#     wav_change_model.wave_change('success.mp3', 0.6, 25.08, os.path.join(current_directory,'media','origin'),os.path.join(current_directory,'media','change'))
#     return render(request, 'audio.html')


def changeaudio(selected_frequency):
    if selected_frequency:
            current_directory = os.path.dirname(os.path.abspath(__file__))
            origin_path = os.path.join(current_directory, 'media', 'origin')
            change_path = os.path.join(current_directory, 'media', 'change')
            
            if selected_frequency == '1':   # 저주파 :20 ~ 1000
                wav_change_model.wave_change('success.mp3', 0.3, 15, origin_path, change_path)
            elif selected_frequency == '2': # 저주파 :20 ~ 2000
                wav_change_model.wave_change('success.mp3', 0.3, 25.08, origin_path, change_path)
            elif selected_frequency == '3': # 중음역 :500 ~ 3000
                wav_change_model.wave_change('success.mp3', 7.5, 31, origin_path, change_path)
            elif selected_frequency == '4': # 고주파 :1000 ~ 20000
                wav_change_model.wave_change('success.mp3', 15, 58.57, origin_path, change_path)
            elif selected_frequency == '5': # 고주파 :2000 ~ 20000
                wav_change_model.wave_change('success.mp3', 25.08, 58.57, origin_path, change_path)
    return 1

# 파일 업로드
@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        print('$$')
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage(os.path.join(current_directory,'media','test'))

        # 주파수 저장
        audio_id = Audio.objects.latest('id').id + 1 if Audio.objects.exists() else 1 # id 얻기
        filename = f"{audio_id}_{uploaded_file.name}"
        fs.save(filename, uploaded_file)

        # 주파수 모드 선택 값 가져오기
        num = request.POST.get('num')
        print(num)
        print(changeaudio(num))
        
        # 입모양 생성 여부 값 가져오기
        generate_mouth = request.POST.get('generate_mouth')
        print(generate_mouth)
        
        # 텍스트 생성 여부 값 가져오기
        generate_text = request.POST.get('generate_text')
        print(generate_text)

        # 파일 확장자 설정
        if generate_mouth == 'yes' or generate_text == 'yes':
            file_extension = 'mp4'
        else:
            file_extension = 'mp3'

        audio = Audio(id=audio_id, path=fs.path(filename)) #모델에 저장
        audio.save()

        message = '파일이 성공적으로 업로드되었습니다.'
        return render(request, 'upload_file.html', {'message': message})
    return render(request, 'upload_file.html')

def result():
    return render(request, 'result.html')

@csrf_exempt
def post(request):
    current_directory = os.path.dirname(os.path.abspath(__file__)) # 현재 경로
    file = request.FILES.get('file')  # 클라이언트에서 전송된 파일 객체를 가져옵니다.
    print(file)
        # 파일 처리 및 저장 로직을 구현합니다.
        # 예를 들어, 파일을 특정 경로에 저장하거나 필요한 처리를 수행합니다.
        # 이 예시에서는 파일을 저장하는 대신 파일 이름을 반환합니다.
    if file:
        file_name = file
        print(file_name)
        return JsonResponse({'file_name': file_name})
    else:
        return JsonResponse({'error': '파일을 찾을 수 없습니다.'}, status=400)
