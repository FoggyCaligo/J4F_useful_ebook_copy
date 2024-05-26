import pyautogui as auto
import time

cursor_currpos = auto.position()

page1 = []
page1.append([230,160])
page1.append([970,970])

page2 = []
page2.append([590,160])
page2.append([1330,970])








def capture():
    auto.hotkey('win','prtsc')

    
    # #start_screeenCapture
    # auto.hotkey('win','shift','s')
    # #drag
    # auto.move(pos1[0], pos1[1])
    # auto.dragTo(pos2[0],pos2[1])
    # auto.click()
    # time.sleep(10)
capture()



