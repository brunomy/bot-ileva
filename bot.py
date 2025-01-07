import pyautogui
import funcoes
import empresas

# Pausa
pyautogui.PAUSE = 0.5 #Pausa Geral

# Run
id = pyautogui.prompt(text='Id empresa', title='PopUp', default='')
funcoes.abrir_navegador(empresas.lista[int(id)])

old_version = pyautogui.prompt(text='Versão antiga', title='PopUp', default='')
version = pyautogui.prompt(text='Versão nova', title='PopUp', default='')
funcoes.clonar_repositorio(empresas.lista[int(id)])

funcoes.mudanca_versao(old_version, version)

funcoes.mudanca_cordova()

funcoes.remove_external()

funcoes.build_apk()

funcoes.build_bundle()

funcoes.excluirRecursoJava()


funcoes.git_commit(version)


