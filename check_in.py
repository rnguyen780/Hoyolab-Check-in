import webbrowser as wb
import pyautogui as ag
from datetime import date

def to_click(button):
    ci_center = ag.center(button)
    ag.click(ci_center.x, ci_center.y)

def switch_games(to_switch, go_to):
    change_game = ag.locateOnScreen(to_switch)
    to_click(change_game)
    to_other = ag.locateOnScreen(go_to)
    to_click(to_other)
 
def check_in(to_check_in, click_on, is_GI):
    ci_button = ag.locateOnScreen(to_check_in)
    to_click(ci_button)

    if is_GI:
        ag.time.sleep(5)
        s = ag.screenshot()
        for x in range(s.width):
            for y in range(s.height):
                if s.getpixel((x, y)) == (215, 132, 90):
                    ag.click(x, y)
                    return
    else:
        ag.time.sleep(6)
        ci_button = ag.locateOnScreen(click_on)
        to_click(ci_button)


if __name__ == '__main__':
    wb.open('https://www.hoyolab.com/home')
    ag.time.sleep(6)

    try: #Genshin check in
        ag.locateOnScreen('Check GI.png')
    except Exception:
        switch_games('Check HSR.png', 'to GI.png')
    check_in('GI 2.png', None, True)
    ag.hotkey('ctrl', 'shift', 'tab')
    ag.time.sleep(1)
    switch_games('Check GI.png', 'to HSR.png')
    check_in('HSR.png', 'HSR Click 2.png', False) #switches to HSR check in
