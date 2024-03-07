import webbrowser as wb
import pyautogui as ag
from datetime import date

def to_click(button, scroll):
    ci_center = ag.center(button)
    ag.click(ci_center.x, ci_center.y)
    if scroll:
        ag.scroll(2)

def switch_tabs(to_switch, go_to):
    ag.hotkey('ctrl', 'shift', 'tab')
    ag.time.sleep(2)
    change_game = ag.locateOnScreen(to_switch)
    to_click(change_game, False)
    to_other = ag.locateOnScreen(go_to)
    to_click(to_other, False)
 
def check_in(to_check_in, load_more, click_on):
    ci_button = ag.locateOnScreen(to_check_in)
    to_click(ci_button, False)

    ag.time.sleep(8)
    if int(date.today().strftime('%m %d %y')[3:5]) > 13:
        ci_button = ag.locateOnScreen(load_more)
        to_click(ci_button, True)
    ag.time.sleep(1)
    ci_button = ag.locateOnScreen(click_on)
    to_click(ci_button, True)

if __name__ == '__main__':
    wb.open('https://www.hoyolab.com/home')
    ag.time.sleep(8)

    try: #Genshin check in
        ag.locateOnScreen('Check GI.png')
        check_in('GI.png', 'GI Load More.png', 'GI Click 2.png')
        switch_tabs('Check GI.png', 'to HSR.png')
        check_in('HSR.png', 'HSR Load More.png', 'HSR Click.png') #switches to HSR check in
    except: #HSR check in
        check_in('HSR.png', 'HSR Load More.png', 'HSR Click.png')
        switch_tabs('Check HSR.png', 'to GI.png')
        check_in('GI.png', 'GI Load More.png', 'GI Click 2.png') #switches to Genshin check in
