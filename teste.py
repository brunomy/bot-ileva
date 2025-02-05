import pyautogui
import time
import funcoes
import os

import empresas

# Pausa
pyautogui.PAUSE = 0.5 #Pausa Geral
# time.sleep(3)

# for i in range(0, 1):
#     print(i)
    
url = os.getcwd()

# funcoes.replace_nano('gitPush.py', 'trocaAquiCaraio', )

pyautogui.alert(text=url, title='asdasd', button='OK')


# Teclado
# pyautogui.keyDown('alt')
# pyautogui.press(['tab'])
# pyautogui.keyUp('alt')
# pyautogui.write('Banana')
# pyautogui.hotkey('ctrl', 'c')
# pyautogui.hotkey('ctrl', 'v')
# pyautogui.hotkey('c')




# Mouse
# pyautogui.click('img/1.png')
# pyautogui.moveTo('img/1.png')
# pyautogui.drag(xOffset=200, yOffset=200, duration=2)
# pyautogui.dragTo(100, 200, 2, button='left')

# function
# def teste():
#     if(pyautogui.locateOnScreen('img/2.png')):
#         print('teste')
#     return

# Pegar tamanho da tela
# screenWidth, screenHeight = pyautogui.size()
# pyautogui.size()

# Pegar posição do mouse
# currentMouseX, currentMouseY = pyautogui.position()
# pyautogui.position()

# Alertas
# pyautogui.confirm(text='oi', title='teste', buttons=['OK', 'Cancel'])
# pyautogui.alert(text='asd', title='asdasd', button='OK')
# print(pyautogui.position())
# senha = pyautogui.password(text='Informe a senha', title='PopUp', default='', mask='*')
# print(senha)
# os.getcwd() #printa pasta atual

# try:
#     while pyautogui.locateOnScreen('img/2.png'):
#         teste()
# except KeyboardInterrupt:
#     print('fim')

