import pyautogui
import os
import time
from pynput.keyboard import Controller
keyboard=Controller()

# Pausa
pyautogui.PAUSE = 0.5 #Pausa Geral

git = 'linkgit'
play = 'linkplay'

def comando(text):
    keyboard.type(text)
    pyautogui.hotkey('enter')

os.system('git push')
os.system('opera')
time.sleep(3)
comando(git)
pyautogui.hotkey('ctrlleft', 't')
comando(play)