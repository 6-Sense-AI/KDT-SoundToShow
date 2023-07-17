# 라이브러리 설치
import openai
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
from moviepy.editor import VideoFileClip
import pysrt
import datetime
import os


# # openai api key

# create_subtitles(audio_path, video_path, srt_path, font_path, res_path):
# 원본 오디오 input, w2l 비디오 input, 자막 생성 path, 폰트 path, 마지막 결과

# openai.api_key = "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"

################################# 오디오에서 .srt 자막 생성하기 ################################# 
def create_subtitles(audio_path, video_path, srt_path, font_path, res_path, changeaudio_path):
    print(audio_path,srt_path)
    openai.api_key = "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"
    audio_file = open(audio_path, "rb")
    transcript = openai.Audio.transcribe(
            file = audio_file,
            model = "whisper-1",
            response_format="srt",
            language="ko"
        )
    print(transcript)

    file = open(srt_path, 'w', encoding="utf-8")    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
    file.write(transcript)      # 파일에 문자열 저장
    file.close()

#################################  .srt 자막을 비디오에 입히기 ################################# 
# def add_subtitles(video_path, srt_path, output_path):
#     current_directory = os.path.dirname(os.path.abspath(__file__))
    video = VideoFileClip(video_path)
    
    subs = pysrt.open(srt_path, encoding='utf-8')
    subtitles = []
    for sub in subs:
        start_time = sub.start.to_time()
        end_time = sub.end.to_time()
        text = sub.text.replace('\n', ' ')  # 줄바꿈 문자 제거
        
        # subtitle_clip = TextClip(text, font='Malgun-Gothic-Bold', fontsize=28, color='black', bg_color='white',
        #                          method='caption', align='center', interline=0, size=(600, 120), stroke_width=1.5)
        # subtitle_clip = subtitle_clip.set_position(('center', 0.82), relative=True).set_duration(
        #     (datetime.timedelta(hours=end_time.hour, minutes=end_time.minute, seconds=end_time.second) -
        #      datetime.timedelta(hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second))
        #     .total_seconds()
        # )
        # 사진관 아저씨
        subtitle_clip = TextClip(text, font='Malgun-Gothic-Bold', fontsize=20, color='black', bg_color='white',
                                 method='caption', align='center', interline=0, size=(350, 100), stroke_width=1.5)
        subtitle_clip = subtitle_clip.set_position(('center', 0.7), relative=True).set_duration(
            (datetime.timedelta(hours=end_time.hour, minutes=end_time.minute, seconds=end_time.second) -
             datetime.timedelta(hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second))
            .total_seconds()
        )        
        subtitle_clip = subtitle_clip.set_start(
            (datetime.timedelta(hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second))
            .total_seconds()
        )
        subtitles.append(subtitle_clip)
    
    videoclip = CompositeVideoClip([video.set_audio(None)] + subtitles, size=video.size)

    # final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')


# add_subtitles(video_path, srt_path, output_path)

# ################################# 자막을 입힌 비디오에 음원 파일 입히기 ################################# 
# # mp3 + mp4
    # videoclip = VideoFileClip(output_path)
    audioclip = AudioFileClip(changeaudio_path) # 입힐 오디오

    videoclip.audio = audioclip # 비디오에 음원 파일 입힘
    # 오디오 길이만큼 영상 자르고, 저장하기
    audio_duration = audioclip.duration
    # videoclip.write_videofile(res_path)
    videoclip.subclip(0, audio_duration).write_videofile(res_path, codec='libx264', audio_codec='aac')


# ################################# 오디오 길이만큼 비디오 자르기 ################################# 
# from pydub import AudioSegment
# from moviepy.editor import VideoFileClip

# # 영상 파일 로드
# video_file = VideoFileClip(res_path)

# # 오디오 파일 로드 및 길이 측정
# audio_file = AudioSegment.from_file(audio_path)
# audio_length = len(audio_file) / 1000  # 밀리초 단위로 길이 변환

# # 영상 자르기
# video_cut = video_file.subclip(0, audio_length)

# # 결과 영상 저장
# video_cut.write_videofile(res_path)