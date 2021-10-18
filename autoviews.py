import pyautogui as pg
from time import sleep


def _startBrowser(url):
    try:
        sleep(2)
        print("Working ")
        pg.press('win')
        sleep(2)
        pg.write("firefox")
        sleep(3)
        pg.press("enter")
        sleep(3)
        pg.write(url)
        pg.press("enter")
        sleep(15)
        pg.press('down', presses=5)
        pg.sleep(2)
        pg.press('down', presses=10)

        sleep(2)
        pg.press('down', presses=5)

        pg.sleep(2)
        pg.press('down', presses=10)
        sleep(2)
        pg.press('down')
        pg.press('down')
        pg.press('down')
        pg.press('down')
        pg.sleep(2)
        pg.press('down')
        pg.press('down')
        pg.press('down')
        pg.press('down')
        sleep(5)
        pg.hotkey('ctrl', 'w')
    except:
        print("Error found")


tm = int(input("How many times it will open ? "))
url = input("Enter website URL")
for xxx in range(0, tm):
    _startBrowser(url)
