import pyautogui
import time

# Pausa
pyautogui.PAUSE = 0.5 #Pausa Geral
# time.sleep(3)

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

# try:
#     while pyautogui.locateOnScreen('img/2.png'):
#         teste()
# except KeyboardInterrupt:
#     print('fim')



def click_terminal():
    pyautogui.click('img/terminal_parado.png')
    pyautogui.moveTo('img/mouse_hover.png')
    


def esperar_terminal():
    pyautogui.keyDown('altleft')
    pyautogui.press('tab')
    pyautogui.keyUp('altleft')
    imagem_concontrada = None
    while imagem_concontrada is None:
        try:
            imagem_concontrada = pyautogui.locateOnScreen('img/terminal_parado.png')
        except:
            print('esperando o terminal finalizar')
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

# 5.6.9
# 5.7.0

# ---------------------------------------------------------------------

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
