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
        
        
    class Color():
        VERDE = '\033[92m'
        VERMELHO = '\033[91m'
        AMARELO = '\033[93m'
        AZUL = '\033[1;34m'
        MAGENTA = '\033[1;35m'
        VERDE_CLARO = '\033[1;92m'
        NEGRITO = '\033[;1m'
        RESET = '\033[0m'


    def function01():
        print(Color.VERMELHO + 'Press Ctrl-C to quit.')
        try:
            while True:
                x, y = pyautogui.position()
                positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
                print(positionStr, end='')
                print('\b' * len(positionStr), end='', flush=True)
        except KeyboardInterrupt:
            print('\n')


    def function02():
        '''pyautogui.press('enter')  # press the Enter key
        pyautogui.press('f1')     # press the F1 key
        pyautogui.press('left')   # press the left arrow key
        pyautogui.hotkey('ctrl', 'alt', 't')
        pyautogui.write('text', interval=0.25,)
        pyautogui.press('enter')
        pyautogui.scroll(10)   # scroll up 10 "clicks"
        pyautogui.scroll(-10)  # scroll down 10 "clicks"
        pyautogui.click(button='right')  # right-click the mouse
        pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)     # start slow, end fast
        pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)    # start fast, end slow
        pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
        pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)   # bounce at the end
        pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # rubber band at the end
        pyautogui.dragTo(100, 200, button='left')     # drag mouse to X of 100, Y of 200 while holding down left mouse button
        pyautogui.dragTo(300, 400, 2, button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
        pyautogui.drag(30, 0, 2, button='right')   # drag the mouse left 30 pixels over 2 seconds while hold
        im2 = pyautogui.screenshot('my_screenshot.png')'''
     
    print(Color.AMARELO + "1 ver localização do mouse")
    print(Color.AMARELO + "2 para executar automação" + Color.RESET)

    x = int(input("digite um numero: "))

    if x == 1:
        try:
            function01()
        except NameError:
            os.system("clear")
            print(Color.VERMELHO + "instale o pyautogui com o pip")


    if x == 2:
        try:
            function02()
        except NameError:
            os.system("clear")
            print(Color.AZUL + "instale o pyautogui com o pip")
            
except KeyboardInterrupt:
    os.system("clear")
    print(Color.VERDE + "o programa foi encerrado!!")

