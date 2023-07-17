from moviepy.editor import *
import openai
import pysrt
import datetime
import os

# # 경로 설정
# audio_path = "input/input_audio.wav"
# video_path = "input/input_video.mp4"
# srt_path = "output/created_sub.srt"    # 자막 생성 결과
# output_path = "output/sub_video.mp4"    # 자막 입힌 영상 결과
# res_path = "res/result.mp4"   # 최종 결과

# # openai api key
# openai.api_key = "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"

current_directory = os.path.dirname(os.path.abspath(__file__))

################################# 오디오에서 .srt 자막 생성하기 ################################# 
def only_text(audio_path, video_path, srt_path, font_path, res_path, changeaudio_path):
    print(audio_path, srt_path)
    openai.api_key = "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"
    audio_file = open(audio_path, "rb")
    transcript = openai.Audio.transcribe(
            file = audio_file,
            model = "whisper-1",
            response_format="srt",
            language="en"
        )
    print(transcript)

    file = open(srt_path, 'w', encoding="utf-8")    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
    file.write(transcript)      # 파일에 문자열 저장
    file.close()

#################################  .srt 자막을 비디오에 입히기 ################################# 
    video = VideoFileClip(video_path)
    
    subs = pysrt.open(srt_path, encoding='utf-8')
    subtitles = []
    for sub in subs:
        start_time = sub.start.to_time()
        end_time = sub.end.to_time()
        text = sub.text.replace('\n', ' ')  # 줄바꿈 문자 제거
        
        subtitle_clip = TextClip(text, font=font_path, fontsize=28, color='black', bg_color='white',
                                 method='caption', align='center', interline=0, size=(600, 120), stroke_width=1.5)
        subtitle_clip = subtitle_clip.set_position(('center', 0.82), relative=True).set_duration(
            (datetime.timedelta(hours=end_time.hour, minutes=end_time.minute, seconds=end_time.second) -
             datetime.timedelta(hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second))
            .total_seconds()
        )
        subtitle_clip = subtitle_clip.set_start(
            (datetime.timedelta(hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second))
            .total_seconds()
        )
        subtitles.append(subtitle_clip)
    
    audioclip = AudioFileClip(changeaudio_path)
    imageclip = ImageClip(os.path.join(current_directory,'cover.jpg'),duration=audioclip.duration)
    videoclip = CompositeVideoClip([imageclip.set_audio(None)] + subtitles, size=video.size)

    # videoclip.write_videofile(output_path, codec='libx264', audio_codec='aac')

# add_subtitles(video_path, srt_path, output_path)

# ################################# 자막을 입힌 비디오에 음원 파일 입히기 ################################# 
    # mp3 + mp4
    # videoclip = VideoFileClip(output_path)
    # audioclip = AudioFileClip(audio_path)

    # videoclip = ImageClip(os.path.join(current_directory,'cover.jpg'),duration=audioclip.duration)
    # videoclip = video.set_audio(audioclip)
    # videoclip.write_videofile(res_path, fps=24, codec="mpeg4")
    
