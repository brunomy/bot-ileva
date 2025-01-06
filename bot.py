import pyautogui
import time

# Pausa
pyautogui.PAUSE = 0.5 #Pausa Geral

# INICIO

def click_terminal():
    pyautogui.click('img/terminal_parado.png')
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
    pyautogui.write(text)
    pyautogui.hotkey('enter')
    
def ctrl_f(old, new):
    time.sleep(2)
    pyautogui.hotkey('ctrlleft', 'f')
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
    pyautogui.write(' ')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrlleft', 's')
    time.sleep(1)
    pyautogui.hotkey('ctrlleft', 's')

def excluirRecursoJava():
    pyautogui.hotkey('win', 'space')
    pyautogui.write('recursos')
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('pagedown')
    pyautogui.hotkey('pageup')
    pyautogui.hotkey('pageup')
    pyautogui.hotkey('pageup')
    pyautogui.hotkey('delete')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    

    

# # 5.6.9
# # 5.7.5

# # ---------------------------------------------------------------------

git_customizado = pyautogui.prompt(text='Link do git', title='PopUp', default='')
nome_pasta = pyautogui.prompt(text='Nome da pasta', title='PopUp', default='')
old_version = pyautogui.prompt(text='Versão antiga', title='PopUp', default='')
version = pyautogui.prompt(text='Versão nova', title='PopUp', default='')

write_external_1 = '<uses-permission android:maxSdkVersion="32" android:name="android.permission.WRITE_EXTERNAL_STORAGE" />'
write_external_2 = '            {              "xml": "<uses-permission android:maxSdkVersion=\"32\" android:name=\"android.permission.WRITE_EXTERNAL_STORAGE\" />",              "count": 1            },'

pyautogui.hotkey('winleft', 't')

comando('cd Home/atualizarAPP/Aplicativos')

comando('git clone git@gitlab.com:hibrida/ileva/app-api.git')

esperar_terminal()

comando('git clone '+git_customizado)

esperar_terminal()

comando('cp -r '+nome_pasta+'/.git app-api/app')

comando('cd app-api/app/')

comando('git restore ./resources ./src/environments config-ios.xml config.xml google-services.json')


comando('code config.xml')

ctrl_f(old_version, version)

click_terminal()

comando('code config-ios.xml')

ctrl_f(old_version, version)

click_terminal()

comando('code ./src/environments/environment.prod.ts')

ctrl_f(old_version, version)

click_terminal()

comando('ionic cordova resources android --icon')

esperar_terminal()

comando('ionic cordova platform rm android')

esperar_terminal()

comando('ionic cordova platform add android@12')

esperar_terminal()

comando('cp google-services.json platforms/android/app/')

comando('code ./platforms/android/app/src/main/AndroidManifest.xml')

ctrl_f(write_external_1, ' ')

click_terminal()

comando('code platforms/android/android.json ')

ctrl_f_external_2()

click_terminal()

comando('code build.json')

ctrl_f('bundle', 'apk')

click_terminal()

comando('ionic cordova build android --prod --release --buildConfig=build.json')

esperar_terminal()

comando('cp platforms/android/app/build/outputs/apk/release/app-release.apk ./../..')

comando('code build.json')

ctrl_f('"apk"', '"bundle"')

click_terminal()

comando('ionic cordova build android --prod --release --buildConfig=build.json')

esperar_terminal()

comando('cp platforms/android/app/build/outputs/bundle/release/app-release.aab ./../..')

comando('git add .')

comando('git status')

comando('git commit -m "'+version+'"')

pyautogui.write('git push')

excluirRecursoJava()
