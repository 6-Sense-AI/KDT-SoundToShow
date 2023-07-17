from django.shortcuts import render
from .models import Audio
from . import cutsound
from . import create_sub
from . import text
from django.core.files.storage import FileSystemStorage
import os
from django.http import HttpResponse ,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .wav2lip import combine_model
from pydub import AudioSegment
# from .wav2lip.combine_model import lip_video_model as lip_video_model
# from ....S2S.Wav2Lip.combine_model import lip_video_model
# import sys
# sys.path.append('..\Wav2Lip')
# from ...Wav2Lip.combine_model import lip_video_model

current_directory = os.path.dirname(os.path.abspath(__file__))

def index(request):
    audio = Audio.objects.all()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    print(audio)
    return render(request, 'index.html', {"audio":audio})

# 오디오 변환
def changeaudio(filename, selected_frequency):
    if selected_frequency:

            origin_path = os.path.join(current_directory, 'static','s2s','audio') # s2s 오디오
            change_path = os.path.join(current_directory, 'static','s2s','audio','change') # s2s 오디오
            
            if selected_frequency == '1':   # 저주파1
                cutsound.cutsd(filename, filename, 20 , 1000, origin_path, change_path)
            elif selected_frequency == '2': # 저주파2
                cutsound.cutsd(filename, filename, 20 , 2000, origin_path, change_path)
            elif selected_frequency == '3': # 원본
                cutsound.cutsd(filename, filename, 0 , 40000, origin_path, change_path)
            elif selected_frequency == '4': # 고주파1
                cutsound.cutsd(filename, filename, 100, 20000, origin_path, change_path)
            elif selected_frequency == '5': # 고주파2
                cutsound.cutsd(filename, filename, 200, 20000, origin_path, change_path)
    return 1

# 파일 업로드
@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        ori_path = os.path.join(current_directory,'static','s2s','audio')

        # 기존에 파일이 존재하면 삭제 (덮어쓰기 기능)
        if os.path.exists(ori_path+'\\test.wav'):
            os.remove(os.path.join(current_directory, 'static','s2s','audio','test.wav'))
        if os.path.exists(ori_path+'\\change\\test.wav'):
            os.remove(os.path.join(current_directory, 'static','s2s','audio','change','test.wav'))

        fs = FileSystemStorage(ori_path) # 입모양에 사용할 음원 따로 저장
        num = request.POST.get('num')
        if num == 3 :
            fs = FileSystemStorage(ori_path+"\\change")

        # 주파수 저장
        audio_id = Audio.objects.latest('id').id + 1 if Audio.objects.exists() else 1 # id 얻기
        filename = f"test.wav" # 오디오 파일 이름
        print(filename)

        fs.save(filename, uploaded_file)
        audio = Audio(id=audio_id, path=fs.path(filename)) #모델에 저장
        audio.save()
        temp = Audio.objects.get(id=audio_id).path
        print(temp)

        # 주파수 모드
        # num = request.POST.get('num')
        print(num)

        changeaudio(filename,num)
        # else :
        #     fs = FileSystemStorage(os.path.join(current_directory, 'static','s2s','audio','change'))
        #     filename = f"test.wav"
        
        # 입모양 생성 여부
        generate_mouth = request.POST.get('generate_mouth')
        print(generate_mouth)
        if generate_mouth == 'yes': # 생성함
            # 원본
            combine_model.lip_video_model(ori_path+'\\'+str(filename),os.path.join(current_directory,'wav2lip','sample_data','base2.mp4'),os.path.join(current_directory,'static','s2s','video')+'\\result.mp4')

        # 텍스트 생성 여부
        generate_text = request.POST.get('generate_text')
        print(generate_text)
        if generate_text == 'yes': # 생성함
            create_sub.create_subtitles(ori_path+'\\test.wav', os.path.join(current_directory,'static','s2s','video')+'\\result.mp4', os.path.join(current_directory,'output')+'\\created_sub.srt', os.path.join(current_directory,'static', 'font')+'\\KCC-Ganpan.woff2', os.path.join(current_directory,'static','s2s','video')+'\\final.mp4',os.path.join(current_directory, 'static','s2s','audio','test.wav'))

        if generate_mouth == 'no' and generate_text == 'yes': # 주파수만 선택된 경우
            print("21341233")
            text.only_text(ori_path+'\\'+str(filename), os.path.join(current_directory+"\\cover.jpg"), os.path.join(current_directory,'output')+'\\created_sub.srt', os.path.join(current_directory,'static', 'font')+'\\KCC-Ganpan.woff2', os.path.join(current_directory,'static','s2s','video')+'\\final.mp4', os.path.join(current_directory, 'static','s2s','audio','change','test.wav'))


# add_subtitles(video_path, srt_path, output_path)
        context = {
            'num': num,
            'generate_mouth': generate_mouth,
            'generate_text': generate_text,
            'filename' : filename,
            'path' : temp,
        }
        message = '파일이 성공적으로 업로드되었습니다.'
        return render(request, 'model_result.html', context)
        # 사용한 파일 삭제
    return render(request, 'upload_file.html')
