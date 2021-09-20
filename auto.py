#python3 auto.py v.02

import pyautogui
import time
import pyautogui, sys
import os

def function01():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')


def function02():
    pyautogui.moveTo(20, 633, 2, pyautogui.easeInQuad)
    time.sleep(2)
    pyautogui.click(x=20, y=633)
    time.sleep(1)
    pyautogui.moveTo(214, 147, 2, pyautogui.easeInQuad)
    pyautogui.click(x=214, y=147)
    time.sleep(1)
    pyautogui.write('ola', interval=0.25,) 
    time.sleep(1)
    pyautogui.moveTo(679, 47, 2, pyautogui.easeInQuad)
    pyautogui.click(x=679, y=47)
    time.sleep(2)
    pyautogui.moveTo(183, 386, 2, pyautogui.easeInQuad)
    pyautogui.click(x=183, y=386)
    time.sleep(2)
    #o codigo abaixo abre o terminal
    pyautogui.hotkey('ctrl', 'alt', 't')
    time.sleep(1)
    pyautogui.moveTo(500, 300, 2, pyautogui.easeInQuad)
    pyautogui.click(x=500, y=300)
    time.sleep(1)
    pyautogui.write('ping 191.7.178.229', interval=0.25,)
    pyautogui.press('enter')

print("1 ver localização do mouse")
print("2 para executar automação")
x = int(input("digite um numero: "))

if x == 1:
    function01()

if x == 2:
    function02()

