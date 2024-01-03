![s2s (2)](https://github.com/6-Sense-AI/KDT-SoundToShow/assets/81418633/60174a33-d9c5-43d7-a358-fa0c358b4d8e)

# KDT-SoundToShow

KDT 해커톤 4회 식스센스 팀 S2S 프로젝트: 경증 청각장애인을 위한 듣기 평가 보조 서비스

## 1. 프로젝트명

- 경증 청각장애인을 위한 청취 보조 서비스
- 서비스설명 : 입력된 음성의 주파수를 변환한 음성, 텍스트와 비디오를 병행 제공한다. librosa로 입력된 음성에서 주파수를 변환한 음성을 반환한다. 또한 입력된 음성을 인식한 후 각각 wav2lip 모델과 Whisper API를 활용, 음성과 동기화된 입모양 영상과 텍스트를 생성해 반환한다. 

## 2. 주요기능

- 가청 주파수 음역대 선택기능 제공
- 영상, 입모양, 자막 생성여부 선택기능 제공
- Librosa 라이브러리를 활용하여 기존 음성을 사용자의 가청 주파수 음역대로 변환
- Wav2Lip 모델을 통해 영상의 입모양 제공
- Whisper OpenAI를 통해 STT 서비스 제공

## 3. 개발환경

|구분|내용|
|------|---|
|사용언어|Python / HTML / CSS / JavaScript|
|사용한 라이브러리|Librosa / PyTorch|
|개발도구|VisualStudioCode / Jupyter / Google Colab|
|데이터베이스|MySQL|

## 4. 아키텍처(구조)
> ####  시스템 아키텍쳐
![시스템 아키텍쳐](https://github.com/6-Sense-AI/KDT-SoundToShow/assets/81418633/6553dd16-ff09-4cc4-99f4-5aed0994ac29)

## 5. 흐름도
> ####  서비스 흐름도 ['영어 듣기 평가 시험' 사례에 서비스 적용을 가정]

![기능흐름도](https://github.com/6-Sense-AI/KDT-SoundToShow/assets/81418633/0b2ebf0c-e2f5-4787-9317-d0bbe77decad)


## 6. 서비스 실행 화면


###  메인 페이지
> ####  시작 화면

![s2s메인](https://github.com/6-Sense-AI/KDT-SoundToShow/assets/87457244/192b03cd-6dc0-4238-baa6-706517ed9763)
> #### 세부 설명
![메인2](https://github.com/6-Sense-AI/KDT-SoundToShow/assets/87457244/ba6cd995-9255-4ae2-b131-e02f6efad4ea)

### 모드 선택 페이지
> #### 파일 업로드 및 모드 선택
![모드선택](https://github.com/6-Sense-AI/KDT-SoundToShow/assets/87457244/3013cbf6-e2ae-4a0b-86be-a05dbbab2a61)
>#### 주파수 모드 선택  [잘 들리는 모드 확인하기]
![잘들리는모드](https://github.com/6-Sense-AI/KDT-SoundToShow/assets/87457244/13e57463-a1bb-46f7-ad6e-4e5f0349942c)

### 결과 페이지
![결과](https://github.com/6-Sense-AI/KDT-SoundToShow/assets/87457244/91e20b10-8379-469e-bed0-c486813a07f1)

## 7. 제작 일정
![image](https://github.com/6-Sense-AI/KDT-SoundToShow/assets/88229105/1bb8b36c-1577-4f59-8dff-811b1c1e27a8)

)


## 8. 팀원 소개 및 담당 업무
![image](https://github.com/6-Sense-AI/KDT-SoundToShow/assets/105771134/ac6b458e-76eb-4985-9dd1-20029a810a19)


