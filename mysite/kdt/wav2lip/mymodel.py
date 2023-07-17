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
from bs4 import BeautifulSoup


def show_video(video_path):
    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def get_video_resolution(video_path):
    """Function to get the resolution of a video"""
    video = cv2.VideoCapture(video_path)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return (width, height)


def resize_video(video_path, new_resolution):
    """Function to resize a video"""
    video = cv2.VideoCapture(video_path)
    fourcc = int(video.get(cv2.CAP_PROP_FOURCC))
    fps = video.get(cv2.CAP_PROP_FPS)
    width, height = new_resolution
    output_path = os.path.splitext(video_path)[0] + '_720p.mp4'
    writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    while True:
        success, frame = video.read()
        if not success:
            break
        resized_frame = cv2.resize(frame, new_resolution)
        writer.write(resized_frame)
    video.release()
    writer.release()

current_directory = os.path.dirname(os.path.abspath(__file__))
PATH_TO_YOUR_VIDEO = os.path.join(current_directory,'sample_data','input_vid.mp4')

# video_duration = mp.VideoFileClip(PATH_TO_YOUR_VIDEO).duration
# if video_duration > 60:
#     print("WARNING: Video duration exceeds 60 seconds. Please upload a shorter video.")
#     raise SystemExit(0)

video_resolution = get_video_resolution(PATH_TO_YOUR_VIDEO)
print(f"Video resolution: {video_resolution}")
if video_resolution[0] >= 1920 or video_resolution[1] >= 1080:
    print("Resizing video to 720p...")
    os.system(f"ffmpeg -i {PATH_TO_YOUR_VIDEO} -vf scale=1280:720 ./sample_data/input_vid.mp4")
    PATH_TO_YOUR_VIDEO = "./sample_data/input_vid.mp4"
    print("Video resized to 720p")
else:
    print("No resizing needed")

resize_video(PATH_TO_YOUR_VIDEO, video_resolution)
# if os.path.isfile(PATH_TO_YOUR_VIDEO):
#     shutil.copyfile(PATH_TO_YOUR_VIDEO, "./sample_data/input_vid.mp4")
#     print("Input Video")


PATH_TO_YOUR_AUDIO = os.path.join(current_directory,'sample_data','test.wav')

# import librosa
# audio, sr = librosa.load(PATH_TO_YOUR_AUDIO, sr=None)

# # # Save audio with specified sampling rate
# import soundfile as sf
# sf.write('./sample_data/input_audio.mp3', audio, sr, format='wav')

# clear_output()

inf_path = os.path.join(current_directory,'inference.py')
chk_path = os.path.join(current_directory,'checkpoints','download.aspx')

# def run_wav2lip(nosmooth, pad_top, pad_bottom, pad_left, pad_right, resize_factor):
#     cmd = [
#         'python',
#         inf_path,
#         '--checkpoint_path', chk_path,
#         '--face', PATH_TO_YOUR_VIDEO,
#         '--audio', PATH_TO_YOUR_AUDIO,
#         '--pads', str(pad_top), str(pad_bottom), str(pad_left), str(pad_right),
#         '--resize_factor', str(resize_factor)
#     ]

#     if not nosmooth:
#         cmd.append('--nosmooth')

#     subprocess.run(cmd)


# Example usage
nosmooth = False
pad_top = 0
pad_bottom = 10
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
print("Final Video Preview")
show_video('./results/result_voice.mp4')
