from django.shortcuts import render
from .models import Audio
from . import wav_change_model
from django.core.files.storage import FileSystemStorage
import os
from django.http import HttpResponse ,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View

def index(request):
    audio = Audio.objects.all()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    print(audio)
    return render(request, 'index.html', {"audio":audio})

def uploadFile(request):
    return render(request,'upload_file.html')

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

@csrf_exempt
def videoUpload(request):
    if request.method == 'POST' and request.FILES['video']:
        uploadFile = request.FILES['video']
        current = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        folder_path = os.path.join(current, 'media/')
        os.makedirs(folder_path, exist_ok=True) # 폴더 생성

        file_path = os.path.join(folder_path, str(uploadFile)) # uploadFile => title
        with open(file_path, 'wb') as destination:
            for chunk in uploadFile.chunks():
                destination.write(chunk)
        return HttpResponse('hello world')

# @csrf_exempt
# def videoUpload(request):
#     if request.method == 'POST' and request.FILES.get('file'):
#         file = request.FILES['file']
#         print(file)
#         id = request.POST['userId']
#         video_title = request.POST['videoTitle']
#         video_address = request.POST['videoAddress']
#         upload_date = request.POST['uploadDate']

#         try: # db저장
#             user = User.objects.get(id=user_id)
#             video = Video(
#                 id=user,
#                 video_title=video_title,
#                 video_addr=video_address,
#                 upload_date=upload_date
#             )
#             video.save()
#             return JsonResponse({'message': 'File uploaded successfully.'})
#         except User.DoesNotExist:
#             return JsonResponse({'message': 'User does not exist.'})
#         except Exception as e:
#             return JsonResponse({'message': 'Error occurred while uploading file.'})

#     else:
#         return JsonResponse({'message': 'File upload failed.'})

# def test(request):
#     wav_change_model('test', 0.6, 25.08, '.', '.')

#     print(audio)
#     return render(request, 'index.html', {"audio":audio})
