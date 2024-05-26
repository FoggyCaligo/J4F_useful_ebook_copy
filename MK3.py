import pyautogui as auto
import time
import keyboard

time.sleep(3)

#카피하고자 하는 책의 페이지 수
page = 330

#다음페이지 버튼 위치
x=921
y=1000

def capture():
    auto.hotkey('win','prtsc')#스크린샷
    auto.click(x,y)#다음페이지 버튼 누르기
    
    # #start_screeenCapture
    # auto.hotkey('win','shift','s')
    # #drag
    # auto.move(pos1[0], pos1[1a])
    # auto.dragTo(pos2[0],pos2[1])
    # auto.click()
    # time.sleep(10)



for i in range(page):
    if keyboard.is_pressed('enter'): break
    capture()


