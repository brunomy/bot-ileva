import pyautogui
import os
import time
from pynput.keyboard import Controller
keyboard=Controller()

# Pausa
pyautogui.PAUSE = 0.5 #Pausa Geral

def comando(text):
    keyboard.type(text)
    pyautogui.hotkey('enter')
    
pyautogui.hotkey('winleft', 't')
pyautogui.hotkey('ctrlleft', 'shiftleft', 't')
comando('cd root/Aplicativos/nomeDaPasta')
comando('git push')
pyautogui.hotkey('ctrlleft', 'shiftleft', 'w')

os.system('opera')
time.sleep(3)
comando('https://gitlab.com/hibrida/ileva/apps-customizados/'+'nomeDaPasta')
pyautogui.hotkey('ctrlleft', 't')
comando('play')