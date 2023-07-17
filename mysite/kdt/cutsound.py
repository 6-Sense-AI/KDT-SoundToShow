import librosa
import numpy as np
import soundfile as sf
'''
input : 변환할 소리파일 경로
output : 저장할 경로
st : 시작 주파수
end : 끝 주파수
'''
def cutsd(input_name, output_name, st, end, input_dir, output_dir):

    # 음악 파일을 로드합니다.
    y,sr = librosa.load(f'{input_dir}\\{input_name}')

    # y,sr = librosa.load(input)
    S = np.abs(librosa.stft(y))
    # mel = librosa.feature.melspectrogram(y=y, sr=sr)

    # 주파수 범위 10~2000
    S[:,0:st] = 0
    S[:,end:] = 0

    # mel to audio
    audio = librosa.griffinlim(S)

    # 음원을 저장합니다.
    # sf.write(output, audio, samplerate=sr)
    sf.write(f'{output_dir}\\{output_name}', audio , samplerate=sr)


# def cutsd(input, output, st, end):
#     y,sr = librosa.load(input)
#     S = np.abs(librosa.stft(y))
#     mel = librosa.feature.melspectrogram(y=y, sr=sr)

#     # 주파수 범위 10~2000
#     mel[:,0:st] = 0
#     mel[:,end:] = 0

#     # mel to audio
#     audio = librosa.feature.inverse.mel_to_audio(mel)

#     # 음원을 저장합니다.
#     sf.write(output, audio, samplerate=sr)
