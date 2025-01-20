# encoding: utf-8
import pyautogui
import time
from pynput.keyboard import Controller
keyboard=Controller()


def click_terminal():
    # pyautogui.click('img/terminal_parado.png')
    pyautogui.hotkey('winleft', 't')
    pyautogui.moveTo('img/mouse_hover.png')
    
def esperar_terminal():
    pyautogui.keyDown('altleft')
    pyautogui.press('tab')
    pyautogui.keyUp('altleft')
    imagem_concontrada = None
    seg = 1
    while imagem_concontrada is None:
        try:
            imagem_concontrada = pyautogui.locateOnScreen('img/terminal_parado.png')
        except:
            print('esperando o terminal\n('+str(seg)+' segundos)')
            seg = seg + 1
    print('comando finalizado')
    click_terminal()
    return

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
    time.sleep(2)
    pyautogui.hotkey('ctrlleft', 'h')
    pyautogui.hotkey('ctrlleft', 'a')
    pyautogui.write('            {')
    pyautogui.hotkey('ctrlleft', 'enter')
    pyautogui.write('              "xml": "<uses-permission android:maxSdkVersion=\\"32\\" android:name=\\"android.permission.WRITE_EXTERNAL_STORAGE\\" />",')
    pyautogui.hotkey('ctrlleft', 'enter')
    pyautogui.write('              "count": 1')
    pyautogui.hotkey('ctrlleft', 'enter')
    pyautogui.write('            },')
    pyautogui.hotkey('tab')
    pyautogui.write(' ')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrlleft', 's')
    time.sleep(1)
    pyautogui.hotkey('ctrlleft', 's')


    
    
    
#Funcoes execução
def clonar_repositorio(emp):
    partesUrl = emp['git'].split('/')
    pasta = partesUrl[-1]

    pyautogui.hotkey('winleft', 't')
    comando('cd ~/Home/atualizarAPP/Aplicativos')
    comando('mkdir '+pasta)
    comando('cd '+pasta)
    comando('git clone git@gitlab.com:hibrida/ileva/app-api.git')
    esperar_terminal()
    comando('git clone '+emp['clone'])
    esperar_terminal()
    comando('cp -r '+pasta+'/.git app-api/app')
    comando('cd app-api/app/')
    comando('git restore ./resources ./src/environments config-ios.xml config.xml google-services.json')
    
def mudanca_versao(old, new):
    comando('code config.xml')
    replace(old, new)
    pyautogui.hotkey('ctrlleft', 'w')
    click_terminal()
    comando('code config-ios.xml')
    replace(old, new)
    pyautogui.hotkey('ctrlleft', 'w')
    click_terminal()
    comando('code ./src/environments/environment.prod.ts')
    replace(old, new)
    pyautogui.hotkey('ctrlleft', 'w')
    click_terminal()

def mudanca_cordova():
    comando('ionic cordova resources android --icon')
    esperar_terminal()
    comando('ionic cordova platform rm android')
    esperar_terminal()
    comando('ionic cordova platform add android@12')
    esperar_terminal()

def remove_external():
    comando('cp google-services.json platforms/android/app/')
    comando('code ./platforms/android/app/src/main/AndroidManifest.xml')
    replace('<uses-permission android:maxSdkVersion="32" android:name="android.permission.WRITE_EXTERNAL_STORAGE" />', ' ')
    pyautogui.hotkey('ctrlleft', 'w')
    click_terminal()
    comando('code platforms/android/android.json ')
    ctrl_f_external_2()
    pyautogui.hotkey('ctrlleft', 'w')
    click_terminal()
    
def build_apk():
    comando('code build.json')
    replace('bundle', 'apk')
    pyautogui.hotkey('ctrlleft', 'w')
    click_terminal()
    comando('ionic cordova build android --prod --release --buildConfig=build.json')
    esperar_terminal()
    comando('cp platforms/android/app/build/outputs/apk/release/app-release.apk ./../..')
    
def build_bundle():
    comando('code build.json')
    replace('"apk"', '"bundle"')
    pyautogui.hotkey('ctrlleft', 'w')
    click_terminal()
    comando('ionic cordova build android --prod --release --buildConfig=build.json')
    esperar_terminal()
    comando('cp platforms/android/app/build/outputs/bundle/release/app-release.aab ./../..')

def excluirRecursoJava():
    pyautogui.hotkey('winleft', 't')
    # comando("chmod +x ~/Home/atualizarAPP/cleanJava.sh")
    comando("kill -9 442545")
    comando("kill -9 443807")
    # pyautogui.hotkey('win', 'space')
    # pyautogui.write('recursos')
    # pyautogui.hotkey('enter')
    # time.sleep(4)
    # pyautogui.hotkey('pagedown')
    # time.sleep(1)
    # pyautogui.hotkey('pageup')
    # pyautogui.hotkey('pageup')
    # pyautogui.hotkey('pageup')
    # pyautogui.hotkey('delete')
    # time.sleep(1)
    # pyautogui.hotkey('down')
    # time.sleep(1)
    # pyautogui.hotkey('enter')
    # time.sleep(1)
    
def abrir_navegador(emp):
    pyautogui.hotkey('winleft', 't')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 't')
    comando('opera')
    time.sleep(3)
    comando(emp['git'])
    pyautogui.hotkey('ctrlleft', 't')
    comando(emp['play'])
    

def git_commit(version):
    pyautogui.hotkey('winleft', 't')
    comando('git add .')
    comando('git status')
    comando('git commit -m "'+version+'"')
    pyautogui.write('git push')
    

    

    