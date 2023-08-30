import time
import keyboard
from PIL import ImageGrab

def screenshot():
    # 2020년 6월 1일 10시 20 분 30초 -> _20200601_102030
    curr_time = time.strftime("+%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time)) # ex) image_20200601_102030.png


keyboard.add_hotkey("F9", screenshot) # 사용자가 F9 키를 누르면 스크린 샷 저장


keyboard.wait("esc") # 사용자가 esc 키를 누를 때까지 프로그램 수행