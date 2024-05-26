import pyautogui as auto
import time

cursor_currpos = auto.position()

page1 = []
page1.append([230,160])
page1.append([970,970])

page2 = []
page2.append([590,160])
page2.append([1330,970])



def test():
    auto.hotkey('win','shift','s')
test()




def capture(pos1,pos2):
    #start_screeenCapture
    auto.hotkey('win','shift','s')
    #drag
    auto.move(pos1[0], pos1[1])
    auto.dragTo(pos2[0],pos2[1])
    auto.click()
    time.sleep(10)



capture(page1[0],page1[1])
capture(page2[0],page2[1])



