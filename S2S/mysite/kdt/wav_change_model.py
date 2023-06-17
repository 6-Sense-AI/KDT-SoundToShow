import librosa
import numpy as np
import soundfile as sf
import os

# music : 음원 파일, st_mel : 시작 멜 단위(주파수로 기준), end_mel : 끝 멜 단위(주파수로 기준), input_dir : 음원파일 주소, output_dir : 저장할 경로

def wave_change(music, st_mel, end_mel, input_dir, output_dir):
    print("wav_change_success")
    '''
    music : 음원 파일 이름
    st_mel : 시작 멜 단위(주파수를 멜단위로 변환) - librosa.hz_to_mel()
    end_mel : 끝 멜 단위(주파수를 멜단위로 변환) - librosa.hz_to_mel()
    '''

    # 음악 파일을 로드합니다.
    data,sr = librosa.load(f'{input_dir}\\{music}')

    S = librosa.feature.melspectrogram(y=data, sr=sr)


    # 40Hz 이상의 2000Hz 이하 주파수를 변경합니다.
    mask = S < st_mel
    S[mask] = st_mel
    mask1 = S > end_mel
    S[mask1] = end_mel


    # Mel_to_stft
    S_ = librosa.feature.inverse.mel_to_stft(S)

    # 음원을 재구성합니다.
    y_ = librosa.istft(S_)

    # 음원을 저장합니다.
    sf.write(f'{output_dir}\\{music}', y_, samplerate=sr)
