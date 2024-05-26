import pyautogui as auto


cursor_currpos = auto.position()


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



