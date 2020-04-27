import cv2
from PIL import Image
import pytesseract
import os
import time
from gtts import gTTS
os.add_dll_directory(r'C:\Program Files (x86)\VideoLAN\VLC')
import vlc


capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# OpenCV [ WARN:0] terminating async callback 해결 방법은 cv2.CAP_DSHOW 를 추가한다.
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
instance = vlc.Instance()
player = instance.media_player_new()


while True:
    ret, frame = capture.read()
    cv2.imshow(""VideoFrame"", frame)
    if cv2.waitKey(1) > 0:
            image = frame
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            filename = ""{}.png"".format(os.getpid())
            cv2.imwrite(filename, gray)
            text = pytesseract.image_to_string(Image.open(filename), lang = 'kor+eng', config = '-c preserve_interword_spaces=1')
            print('--------------------------')
            print(text)
            print('--------------------------')
            os.remove(filename)
            cv2.imshow(""Output"",gray)
            try:
                    tts = gTTS(text=text, lang ='ko')
                    tts.save(""test.mp3"")
                    media = instance.media_new('test.mp3')
                    player.set_media(media)
                    player.play()
                    time.sleep(1)

            except AssertionError:
                    print(""AssertionError: No text to speak"")

            if cv2.waitKey(1) > 0:
                    break


capture.release()
cv2.destroyAllWindows()