import os
import shutil
from IPython.display import HTML, clear_output
from base64 import b64encode
import moviepy.editor as mp
import cv2
import subprocess
from IPython import display
import numpy as np
from scipy.io.wavfile import read as wav_read
import io
import ffmpeg
from base64 import b64decode
import moviepy.editor as moviepy
from moviepy.editor import *
'''
audio : audio 경로
video : video 경로
result_path : output 경로
'''
def lip_video_model(audio, video, result):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    print(current_directory)
    PATH_TO_YOUR_VIDEO = os.path.join(current_directory, video)
    PATH_TO_YOUR_AUDIO = os.path.join(current_directory,audio)
    inf_path = os.path.join(current_directory,'inference.py')
    chk_path = os.path.join(current_directory,'checkpoints','download.aspx')

    nosmooth = False
    pad_top = 0
    pad_bottom = 0
    pad_left = 0
    pad_right = 0
    resize_factor = 1

    if nosmooth == False:
        # subprocess.call(['cd', '../Wav2Lip'])
        subprocess.call(['python', inf_path, '--checkpoint_path', chk_path, '--face', PATH_TO_YOUR_VIDEO, '--audio', PATH_TO_YOUR_AUDIO, '--pads', str(pad_top), str(pad_bottom), str(pad_left), str(pad_right), '--resize_factor', str(resize_factor)])
    else:
        # subprocess.call(['cd', '../Wav2Lip'])
        subprocess.call(['python', inf_path, '--checkpoint_path', chk_path, '--face', PATH_TO_YOUR_VIDEO, '--audio', PATH_TO_YOUR_AUDIO, '--pads', str(pad_top), str(pad_bottom), str(pad_left), str(pad_right), '--resize_factor', str(resize_factor), '--nosmooth'])

    clear_output()
    # print("Final Video Preview")
    
    video_pth = os.path.join(current_directory, 'temp/result.avi')   # Wav2Lip 결과 영상
    audio_pth = audio    # 합칠 오디오 파일

    mp4_pth = os.path.join(current_directory, 'temp/change.mp4')    # mp4로 변환된 영상
    result_pth = os.path.join(current_directory, result)    # 오디오와 합쳐 최종적으로 출력되는 mp4 파일
    
    # avi to mp4
    clip = moviepy.VideoFileClip(video_pth)
    clip.write_videofile(mp4_pth)

    # mp3 + mp4
    videoclip = VideoFileClip(mp4_pth)
    audioclip = AudioFileClip(audio_pth)

    videoclip.audio = audioclip
    videoclip.write_videofile(result_pth)
    
    return result_pth

# lip_video_model(os.path.join(current_directory, 'haha','test.wav'),os.path.join(current_directory,'sample_data','input_vid.mp4'),'results/hello.mp4')