import pyautogui as pyautogui
from time import sleep

def gotodvornik():
    sleep(5)
    pyautogui.screenshot('C:/Users/Admin/Desktop/maks/items/example.png')
    pyautogui.locateOnScreen('items/Earth.png')
    pyautogui.click('items/Earth.png')
    sleep(1.5)
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/Professions.png')
    pyautogui.click('items/Professions.png')
    sleep(1.5)
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/Dvornik.png')
    pyautogui.click('items/Dvornik.png')
    sleep(9)

def FullScreen():
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/Settings.png')
    pyautogui.click('items/Settings.png')
    sleep(1.6)
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/Full.png')
    pyautogui.click('items/Full.png')
    sleep(1.5)
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/accept.png')
    pyautogui.click('items/accept.png')


ranger = 8


def Workdvornik():
    pyautogui.screenshot('items/example.png')
    try:
        for i in range(8):
            pyautogui.locateAllOnScreen('items/lusha.png',confidence=1)
            pyautogui.click('items/lusha.png')
            sleep(0.6)
    except (RuntimeError,TypeError,NameError):
        print('lusha кончились. Продолжаю поиск...')
    try:
        for i in range(8):
            pyautogui.locateAllOnScreen('items/paper.png')
            pyautogui.click('items/paper.png')
            sleep(0.6)
    except (RuntimeError,TypeError,NameError):
        print('paper кончились. Продолжаю поиск...')
    try:
        for i in range(8):
            print("не нашел")
            pyautogui.locateOnScreen('items/banka.png')
            pyautogui.click('items/banka.png')
            sleep(0.6)
    except (RuntimeError,TypeError,NameError):
        print('banka кончилась. Продолжаю поиск...')
        for i in range(2):
            for i in range(15):
                a = 1
                sleep(10)
                gotodvornik()
                sleep(5)
                Workdvornik()
                sleep(20)
                a += 1
            if a > 14:
                pass

def farmer():
    FullScreen()
    gotodvornik()
    Workdvornik()

farmer()