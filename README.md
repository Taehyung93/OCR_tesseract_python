# 개요

tesseract 소개 : https://ko.wikipedia.org/wiki/테서랙트

```
해당 python script 의 기능 설명 

1. 우선 openCV 을 이용하여 웹캠을 통해 비춰진 사진을 찍는다.
2. 그 사진에 찍힌 것을 tesseract 라이브러리를 통해 문자로 변환한다.
3. 문자로 변환한 것을 Google TTS 라이브러리를 통해 mp3 파일로 만든다.
4. mp3 파일을 VLC player 라이브러리를 통해 재생한다.

즉 사진에 찍힌 문자를 음성으로 변환해주는 기능이다.

tesseract 오픈소스를 연구해보기위해 다양한 옵션값들을 적용해보면서 만들어보았다.
```

# 설치

### 공통사항
```
가상환경은 사용하지 않는다고 가정하고 설치한다.

python 이 32 bit 버전이면, vlc player 도 32 bit 버전으로 다운받아주어야한다.
```


### Windows10
```
Windows tesseract 설치주소: https://github.com/UB-Mannheim/tesseract/wiki
언어팩 항목에 Korean 을 꼭 클릭해주고 설치를 진행하자.
C:\Program Files (x86)\Tesseract-OCR
상기와 같이 설치 주소를 환경변수까지 등록해야된다.

$ python -m pip install opencv-python
$ python -m pip install python-vlc
$ python -m pip install pytesseract
$ python -m pip install gTTS 
$ python -m pip install Pillow
```

### Ubuntu 18.04
```
openCV 설치 방법 링크: https://webnautes.tistory.com/1186

$ sudo apt install tesseract-ocr -y
$ sudo apt-get install tesseract-ocr-script-hang tesseract-ocr-script-hang-vert -y
$ sudo pip3 install pytesseract
$ sudo pip3 install gTTS 
$ sudo pip3 install Pillow
$ sudo pip3 install python-vlc
```

# 코드 설명

### 공통사항
```
text = pytesseract.image_to_string(Image.open(filename), lang = 'Hangul', config = '-c preserve_interword_spaces=1')
상기 부분이 tesseract 가 동작하는 부분이며, config 가 옵션 값을 넣는 부분이다.
preserve_interword_spaces=1 은 띄어쓰기를 인식하게 한다는 옵션이다.

--psm N 을 config 에 추가할 수 있으며, 없으면 default psm 이 적용된다.
```

### Windows10
```
os.add_dll_directory(r'C:\Program Files (x86)\VideoLAN\VLC')
상기 코드를 vlc 를 import 하기전에 해서 vlc 주소를 알려줘야한다.

windows 언어옵션에 Hangul 대신 kor 를 넣으면 된다.

cv2.waitKey(1) > 0 은 아무 키나 한 번 눌러도 잘 먹는데, 
cv2.waitKey(1) == 76 이런 식으로 하면 잘 먹지 않는다. 계속 그 키를 쭉 누르고 있어야 겨우 먹는다.
그래서 cv2.waitKey(1) > 0 방식으로 코딩을 해주었다.
실행했을 때 아무키나 한 번 누르면 찍히고 기능이 동작하며, 아무키나 동시에 두 번 누르면 캠이 꺼지며 python script 가 종료된다.
```

### Ubuntu 18.04
```
Ubuntu 는 언어옵션에 kor 대신 Hangul 를 넣으면 된다.

s 를 누르면 사진이 찍히고 동작이되먀, q 를 누르면 종료가된다.
```

## 참고
```
--psm N
psm 옵션 설명

0 = Orientation and script detection (OSD) only.
1 = Automatic page segmentation with OSD.
2 = Automatic page segmentation, but no OSD, or OCR. (not implemented)
3 = Fully automatic page segmentation, but no OSD. (Default)
4 = Assume a single column of text of variable sizes.
5 = Assume a single uniform block of vertically aligned text.
6 = Assume a single uniform block of text.
7 = Treat the image as a single text line.
8 = Treat the image as a single word.
9 = Treat the image as a single word in a circle.
10 = Treat the image as a single character.
11 = Sparse text. Find as much text as possible in no particular order.
12 = Sparse text with OSD.
13 = Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.

psm 주기 제일 좋은 것은 하나의 문자 -> 단어 -> 문장 순이다. 
문서 전체는 매우 formatic 한 형태가 아니면 한글은 잘 먹지 않는다.

터미널에서 바로 tesseract 돌려보기 
사진이 경로에 있어야되며, Windows10 은 환경변수 등록이 되어있어야한다.
Ubuntu: tesseract -c preserve_interword_spaces=1 test.jpeg stdout -l Hangul
Windows10: tesseract -c preserve_interword_spaces=1 test.jpeg stdout -l kor 

```
## 추후 개발 사항
```
사진을 찍고 ocr 돌리는 부분이므로, 사진을 찍었을 때 문서부분을 openCV 를 이용해 distortion 해서 조정하고 윤곽선을 잡게한다.
ROI 를 잡고 찍어도 되겠다.

사용자가 정말 필요로하는 소프트웨어에 대한 고민을 하며 추후 개발 사항을 고려해봐야겠다.
```
