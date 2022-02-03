#python3 auto.py v.02
try:
    import os
    try:
        import pyautogui
        import time
        import pyautogui, sys
    except ModuleNotFoundError:
        os.system("clear")
        print("instale o pyautogui com o pip")
        
        
class color():
    VERDE = '\033[92m'
    VERMELHO = '\033[91m'
    AMARELO = '\033[93m'
    AZUL = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    VERDE_CLARO = '\033[1;92m'
    NEGRITO = '\033[;1m'
    RESET = '\033[0m'


    def function01():
        print(color.VERMELHO + 'Press Ctrl-C to quit.')
        try:
            while True:
                x, y = pyautogui.position()
                positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
                print(positionStr, end='')
                print('\b' * len(positionStr), end='', flush=True)
        except KeyboardInterrupt:
            print('\n')


    def function02():
     '''pyautogui.moveTo(20, 633, 2, pyautogui.easeInQuad)
        time.sleep(2)
        pyautogui.click(x=20, y=633)
        time.sleep(1)
        pyautogui.click(x=214, y=147)
        time.sleep(1)
        pyautogui.write('ola', interval=0.25,) 
        time.sleep(1)
        pyautogui.click(x=679, y=47)
        time.sleep(2)
        pyautogui.click(x=183, y=386)
        time.sleep(2)
        #o codigo abaixo abre o terminal
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(1)
        pyautogui.click(x=500, y=300)
        time.sleep(1)
        pyautogui.write('teste', interval=0.25,)
        pyautogui.press('enter')'''

    print("1 ver localização do mouse")
    print("2 para executar automação")

    x = int(input("digite um numero: "))

    if x == 1:
        try:
            function01()
        except NameError:
            os.system("clear")
            print(color.VERMELHO + "instale o pyautogui com o pip")


    if x == 2:
        try:
            function02()
        except NameError:
            os.system("clear")
            print(color.VERMELHO + "instale o pyautogui com o pip")
            
except KeyboardInterrupt:
    os.system("clear")
    print(color.VERDE + "o programa foi encerrado!!")

