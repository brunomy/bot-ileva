import pyautogui
import funcoes
import empresas
import os

# Pausa
pyautogui.PAUSE = 0.5 #Pausa Geral

# Run
id = pyautogui.prompt(text='Id empresa', title='PopUp', default='')
# funcoes.abrir_navegador(empresas.lista[int(id)])

old_version = pyautogui.prompt(text='Versão antiga', title='PopUp', default='5.8.0')
version = pyautogui.prompt(text='Versão nova', title='PopUp', default='5.8.1')

funcoes.clonar_repositorio(empresas.lista[int(id)])

funcoes.mudanca_versao(old_version, version)

funcoes.mudanca_cordova()

funcoes.remove_external()

funcoes.build_apk(empresas.lista[int(id)])

funcoes.build_bundle(empresas.lista[int(id)])

funcoes.excluirRecursoJava()

funcoes.git_commit(version, empresas.lista[int(id)])