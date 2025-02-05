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
    
def replace_nano(arquivo, old, new):
    pyautogui.hotkey('winleft', 't')
    comando('nano '+arquivo)
    time.sleep(1)
    # pyautogui.hotkey('s')pwd
    pyautogui.hotkey('ctrlleft', '\\')
    comando(old)
    comando(new)
    pyautogui.hotkey('t')
    pyautogui.hotkey('ctrlleft', 'o')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrlleft', 'x')


def remove_external_nano():
    pyautogui.hotkey('winleft', 't')
    comando('nano platforms/android/android.json')
    time.sleep(1)
    pyautogui.hotkey('ctrlleft', 'w')
    comando('"xml": "<uses-permission android:maxSdkVersion=\\"32\\" android:name=\\"android.permission.WRITE_EXTERNAL_STORAGE\\" />"')
    pyautogui.hotkey('up')
    pyautogui.hotkey('ctrlleft', 'k')
    pyautogui.hotkey('ctrlleft', 'k')
    pyautogui.hotkey('ctrlleft', 'k')
    pyautogui.hotkey('ctrlleft', 'k')
    pyautogui.hotkey('ctrlleft', 'o')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrlleft', 'x')



    
#Funcoes execução

def clonar_repositorio(nome, root):

    pyautogui.hotkey('winleft', 't')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 't')
    
    comando('cd '+root+'/Aplicativos')
    os.chdir('Aplicativos')
    comando('mkdir '+nome)
    comando('cd '+nome)
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')
    os.system('git clone git@gitlab.com:hibrida/ileva/app-api.git')
    os.chdir(nome)
    os.system('git clone git@gitlab.com:hibrida/ileva/apps-customizados/'+nome+'.git')
    time.sleep(1)
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')
    comando('cp -r ../app-api/app ./')
    comando('cp -r '+nome+'/.git ./app')
    comando('cd app')
    os.chdir('app')
    comando('git restore ./resources ./src/environments config-ios.xml config.xml google-services.json')
    comando('git restore ./publicacao')
    
def mudanca_versao(old, new):
    replace_nano('config.xml', old, new)
    replace_nano('config-ios.xml', old, new)
    replace_nano('./src/environments/environment.prod.ts', old, new)

def conf_cordova():
    pyautogui.hotkey('winleft', 't')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')
    os.system('ionic cordova resources android --icon')
    os.system('ionic cordova platform rm android')
    os.system('ionic cordova platform add android@12')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')


def remove_external():
    pyautogui.hotkey('winleft', 't')
    comando('cp google-services.json platforms/android/app/')
    replace_nano('platforms/android/app/src/main/AndroidManifest.xml', '<uses-permission android:maxSdkVersion="32" android:name="android.permission.WRITE_EXTERNAL_STORAGE" />', ' ')
    time.sleep(2)
    remove_external_nano()
    time.sleep(2)
    
def build_apk(nome):
    pyautogui.hotkey('winleft', 't')
    replace_nano('build.json', '"bundle"', '"apk"')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')
    os.system('ionic cordova build android --prod --release --buildConfig=build.json')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')
    comando('mv platforms/android/app/build/outputs/apk/release/app-release.apk ./../'+nome+'.apk')
    
def build_bundle(nome):
    pyautogui.hotkey('winleft', 't')
    replace_nano('build.json', '"apk"', '"bundle"')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')
    os.system('ionic cordova build android --prod --release --buildConfig=build.json')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')
    comando('mv platforms/android/app/build/outputs/bundle/release/app-release.aab ./../'+nome+'.aab')

def excluirRecursoJava():
    pyautogui.hotkey('winleft', 't')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')
    os.system("killall java")
    # os.system("killall code")
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')

def git_commit(version, nome):
    pyautogui.hotkey('winleft', 't')
    comando('git add .')
    comando('git status')
    comando('git commit -m "'+version+'"')
    os.chdir('../../..')
    comando('cp -r .git ..')
    comando('cd ..')
    comando('rm -rf app')
    time.sleep(3)
    comando('rm -rf '+nome)
    time.sleep(3)

    
def abrir_navegador(emp, root):
    os.system('cp ./gitPush.py ./Aplicativos/'+emp['nome'])
    time.sleep(1)
    
    os.chdir('Aplicativos/'+emp['nome'])

    replace_nano('gitPush.py', 'nomeDaPasta', emp['nome'])
    replace_nano('gitPush.py', 'play', emp['play'])
    replace_nano('gitPush.py', 'root', root)
    
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')
    
    os.system('pyinstaller --onefile --windowed gitPush.py')
    os.system('cp ./dist/gitPush ./')
    os.chdir('../..')
    
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'tab')
    
    comando('rm -rf dist')
    comando('rm -rf build')
    comando('rm -rf gitPush.spec')
    comando('rm -rf gitPush.py')
    
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'w')

