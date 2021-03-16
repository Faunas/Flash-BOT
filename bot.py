import pyautogui
from time import sleep

def zagruska():
    pyautogui.screenshot('items/example.png')
    im = pyautogui.locateOnScreen('items/loading.png')
    try:
        while im:
            pyautogui.screenshot('items/example.png')
            sleep(1)
            zagruska()
    except (RuntimeError,TypeError,NameError):
        print('Загрузка завершена. Перехожу в Аватарию.')


def finddone():
    im = pyautogui.locateOnScreen('items/Done.png')
    try:
        im
        sleep(5)
        pyautogui.doubleClick('items/Done.png')
    except (RuntimeError,TypeError,NameError):
        finddone()


def OpenGame():
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/gamelogo.png')
    pyautogui.doubleClick('items/gamelogo.png')
    sleep(7)
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/mygames.png')
    pyautogui.click('items/mygames.png')
    sleep(4)
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/Avataria.png')
    pyautogui.click('items/Avataria.png')
    sleep(5)
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/Play.png')
    pyautogui.click('items/Play.png')
    sleep(2)
    pyautogui.locateOnScreen('items/line.png')
    sleep(1)
    pyautogui.doubleClick(x=1348,y=383)
    finddone()
    sleep(10)
    pyautogui.doubleClick(x=1348,y=333)
    sleep(60)
    pyautogui.screenshot('items/example.png')
    try:
        pyautogui.locateOnScreen('items/krest.png')
        pyautogui.click('items/krest.png')
    except (RuntimeError,TypeError,NameError):
        print('Продолжаем')
    try:
        pyautogui.locateOnScreen('items/firstzakrit.png')
        pyautogui.click('items/firstzakrit.png')
    except (RuntimeError,TypeError,NameError):
        print('Продолжаем')
    try:
        pyautogui.locateOnScreen('items/takepresent.png')
        pyautogui.click('items/takepresent.png')
    except (RuntimeError,TypeError,NameError):
        print('Продолжаем')


def gotodvornik():
    sleep(5)
    pyautogui.screenshot('items/example.png')
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
def Loading():
    try:
        pyautogui.screenshot('items/example.png')
        if z:
            pyautogui.screenshot('items/example.png')
            sleep(1)
            pyautogui.locateOnScreen('items/loading.png')
            sleep(1)
        else:
            Loading()
    except (RuntimeError,TypeError,NameError):
        print(RuntimeError,TypeError,NameError)
        pass


def Energy():
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/people.png')
    pyautogui.click('items/people.png')
    sleep(20)
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/home.png')
    pyautogui.click('items/home.png')
    sleep(1)
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/homepage.png')
    pyautogui.click('items/homepage.png')
    sleep(1)
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/homedone.png')
    pyautogui.click('items/homedone.png')
    sleep(1)
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/fridge.png')
    pyautogui.click('items/fridge.png')
    sleep(1)
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/eat.png')
    pyautogui.click('items/eat.png')
    pyautogui.locateOnScreen('items/fridge1.png')
    pyautogui.click('items/fridge1.png')
    sleep(1)
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/eat.png')
    pyautogui.click('items/eat.png')


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
    sleep(5)
    pyautogui.screenshot('items/example.png')
    try:
        for i in range(8):
            pyautogui.locateAllOnScreen('items/lusha.png',confidence=1)
            pyautogui.click('items/lusha.png')
    except (RuntimeError,TypeError,NameError):
        print('lusha кончились. Продолжаю поиск...')
    try:
        for i in range(8):
            pyautogui.locateAllOnScreen('items/paper.png')
            pyautogui.click('items/paper.png')
    except (RuntimeError,TypeError,NameError):
        print('paper кончились. Продолжаю поиск...')
    try:
        for i in range(8):
            print("не нашел")
            pyautogui.locateOnScreen('items/banka.png')
            pyautogui.click('items/banka.png')
    except (RuntimeError,TypeError,NameError):
        print('banka кончилась. Продолжаю поиск...')
        for i in range(2):
            for i in range(100):
                a = 1
                sleep(10)
                gotodvornik()
                sleep(5)
                Workdvornik()
                sleep(20)
                a += 1
            if a > 99:
                pass





def gotosadovod():
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/Earth.png')
    pyautogui.click('items/Earth.png')
    sleep(2)
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/Professions.png')
    pyautogui.click('items/Professions.png')
    sleep(2)
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/sadovod.png')
    pyautogui.click('items/sadovod.png')
    sleep(5)


def Worksadovod():
    #FullScreen()
    sleep(2)
    pyautogui.screenshot('items/example.png')
    try:
        for i in range(ranger):
            pyautogui.locateOnScreen('items/bigkust.png')
            pyautogui.click('items/bigkust.png')
    except (RuntimeError,TypeError,NameError):
        print('bigkust не нашёл.')
    try:
        for i in range(ranger):
            pyautogui.locateOnScreen('items/smallkust.png')
            pyautogui.click('items/smallkust.png')
    except (RuntimeError,TypeError,NameError):
        print('smallkust не нашёл.')
    try:
        for i in range(ranger):
            pyautogui.locateOnScreen('items/smallkust2.png')
            pyautogui.click('items/smallkust2.png')
    except (RuntimeError,TypeError,NameError):
        print('smallkust2 не нашёл.')
    try:
        for i in range(ranger):
            pyautogui.locateOnScreen('items/smallkust3.png')
            pyautogui.click('items/smallkust3.png')
    except (RuntimeError,TypeError,NameError):
        print('smallkust3 не нашёл.')
    try:
        for i in range(ranger):
            pyautogui.locateOnScreen('items/longkust.png')
            pyautogui.click('items/longkust.png')
    except (RuntimeError,TypeError,NameError):
        print('longkust не нашёл.')
    try:
        for i in range(ranger):
            pyautogui.locateOnScreen('items/zhuk.png')
            pyautogui.click('items/zhuk.png')
    except (RuntimeError,TypeError,NameError):
        print('zhuk не нашёл.')
        try:
            for i in range(ranger):
                pyautogui.locateOnScreen('items/purpleroza.png')
                pyautogui.click('items/purpleroza.png')
        except (RuntimeError,TypeError,NameError):
            print('purpleroza не нашёл.')
            blueflower()
        sleep(2)

def blueflower():
    for i in range(ranger):
        try:
            for i in range(ranger):
                pyautogui.screenshot('items/example.png')
                pyautogui.locateAllOnScreen('items/blueflower.png')
                pyautogui.click('items/blueflower.png')
        except (RuntimeError,TypeError,NameError):
            print('blueflower не нашёл.')

def clicker():
    FullScreen()
    ac= 1
    while ac > 0:
        pyautogui.screenshot('items/example.png')
        pyautogui.locateOnScreen('items/snegovik.png')
        pyautogui.doubleClick('items/snegovik.png')

def farmer():
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/Earth.png')
    pyautogui.click('items/Earth.png')
    sleep(5)
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/street.png')
    pyautogui.click('items/street.png')
    sleep(15)
    pyautogui.screenshot('items/example.png')
    try:
        pyautogui.locateOnScreen('items/newyear.png')
        pyautogui.click('items/newyear.png')
        sleep(10)
    except (RuntimeError,TypeError,NameError):
        print('Время не прошло')
        beg()
    beg()
def beg():
    from time import sleep
    seconds_left = 9999999
    while seconds_left > 0:
        beg1()
        sleep(1)
        print(seconds_left)
def beg1():
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/People.png')
    pyautogui.click(x=370, y=715)
    sleep(50)
    pyautogui.screenshot('items/example.png')
    pyautogui.locateOnScreen('items/home1.png')
    pyautogui.click('items/home1.png')
    sleep(50)
    sadovod()
    sleep(2)
    farmer()

def sadovod():
    gotosadovod()
    Worksadovod()

def dvornik():
    gotodvornik()
    Workdvornik()
    sleep(0.3)

def randomwork():
    sadovo = 1
    dvorni = 0
    if random.random():
        print(random.random)
        sadovod()
    else:
        dvornik()
        print(random.random)

#OpenGame()
#randomwork()
FullScreen()
#Workdvornik()
dvornik()
#farmer()
