# encoding: utf-8
import pyautogui
import time
from pynput.keyboard import Controller
keyboard=Controller()
import os

def comando(text):
    keyboard.type(text)
    # keyboard.write(text)
    pyautogui.hotkey('enter')
    
def replace(old, new):
    time.sleep(2)
    pyautogui.hotkey('ctrlleft', 'h')
    pyautogui.hotkey('ctrlleft', 'a')
    pyautogui.write(old)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrlleft', 'a')
    pyautogui.write(new)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrlleft', 's')
    time.sleep(1)
    pyautogui.hotkey('ctrlleft', 's')
    
def ctrl_f_external_2():
    time.sleep(3)
    pyautogui.hotkey('ctrlleft', 'f')
    pyautogui.hotkey('ctrlleft', 'a')
    pyautogui.write('            {')
    pyautogui.hotkey('ctrlleft', 'enter')
    pyautogui.write('              "xml": "<uses-permission android:maxSdkVersion=\\"32\\" android:name=\\"android.permission.WRITE_EXTERNAL_STORAGE\\" />",')
    pyautogui.hotkey('ctrlleft', 'enter')
    pyautogui.write('              "count": 1')
    pyautogui.hotkey('ctrlleft', 'enter')
    pyautogui.write('            },')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrlleft', 'a')
    pyautogui.write(' ')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrlleft', 's')
    time.sleep(1)
    pyautogui.hotkey('ctrlleft', 's')
    
    
#Funcoes execução
def abrir_navegador(emp):
    pyautogui.hotkey('winleft', 't')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 't')
    os.system('opera')
    time.sleep(3)
    comando(emp['git'])
    pyautogui.hotkey('ctrlleft', 't')
    comando(emp['play'])

def clonar_repositorio(emp):
    partesUrl = emp['git'].split('/')
    pasta = partesUrl[-1]
    
    pyautogui.hotkey('winleft', 't')
    comando('cd ~/Home/atualizarAPP/Aplicativos')
    comando('mkdir '+pasta)
    comando('cd '+pasta)
    os.chdir('Aplicativos/'+pasta)
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')
    os.system('git clone git@gitlab.com:hibrida/ileva/app-api.git')
    os.system('git clone '+emp['clone'])
    time.sleep(1)
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')
    comando('cp -r '+pasta+'/.git app-api/app')
    comando('cd app-api/app/')
    os.chdir('app-api/app/')
    comando('git restore ./resources ./src/environments config-ios.xml config.xml google-services.json')
    
def mudanca_versao(old, new):
    pyautogui.hotkey('winleft', 't')
    comando('code config.xml')
    replace(old, new)
    pyautogui.hotkey('ctrlleft', 'w')
    pyautogui.hotkey('winleft', 't')
    comando('code config-ios.xml')
    replace(old, new)
    pyautogui.hotkey('ctrlleft', 'w')
    pyautogui.hotkey('winleft', 't')
    comando('code ./src/environments/environment.prod.ts')
    replace(old, new)
    pyautogui.hotkey('ctrlleft', 'w')
    pyautogui.hotkey('winleft', 't')

def mudanca_cordova():
    pyautogui.hotkey('winleft', 't')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')
    os.system('ionic cordova resources android --icon')
    os.system('ionic cordova platform rm android')
    os.system('ionic cordova platform add android@12')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')


def remove_external():
    pyautogui.hotkey('winleft', 't')
    comando('cp google-services.json platforms/android/app/')
    comando('code ./platforms/android/app/src/main/AndroidManifest.xml')
    replace('<uses-permission android:maxSdkVersion="32" android:name="android.permission.WRITE_EXTERNAL_STORAGE" />', ' ')
    pyautogui.hotkey('ctrlleft', 'w')
    pyautogui.hotkey('winleft', 't')
    comando('code platforms/android/android.json ')
    ctrl_f_external_2()
    pyautogui.hotkey('ctrlleft', 'w')
    
def build_apk(emp):
    partesUrl = emp['git'].split('/')
    pasta = partesUrl[-1]
    
    pyautogui.hotkey('winleft', 't')
    comando('code build.json')
    replace('bundle', 'apk')
    pyautogui.hotkey('ctrlleft', 'w')
    pyautogui.hotkey('winleft', 't')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')
    os.system('ionic cordova build android --prod --release --buildConfig=build.json')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')
    comando('mv platforms/android/app/build/outputs/apk/release/app-release.apk ./../../'+pasta+'.apk')
    
def build_bundle(emp):
    partesUrl = emp['git'].split('/')
    pasta = partesUrl[-1]

    pyautogui.hotkey('winleft', 't')
    comando('code build.json')
    replace('"apk"', '"bundle"')
    pyautogui.hotkey('ctrlleft', 'w')
    pyautogui.hotkey('winleft', 't')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')
    os.system('ionic cordova build android --prod --release --buildConfig=build.json')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')
    comando('mv platforms/android/app/build/outputs/bundle/release/app-release.aab ./../../'+pasta+'.aab')

def excluirRecursoJava():
    pyautogui.hotkey('winleft', 't')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')
    os.system("killall java")
    os.system("killall code")
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')


def git_commit(version):
    pyautogui.hotkey('winleft', 't')
    comando('git add .')
    comando('git status')
    comando('git commit -m "'+version+'"')
    pyautogui.write('git push')
    

    

    