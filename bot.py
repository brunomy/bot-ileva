import pyautogui
import funcoes
import empresas
import os

# Pausa
pyautogui.PAUSE = 0.5 #Pausa Geral

# Run
inicio = pyautogui.prompt(text='Início', title='Selecione o range', default='')
fim = pyautogui.prompt(text='Fim', title='Selecione o range', default='')

old_version = pyautogui.prompt(text='Versão antiga', title='PopUp', default='5.8.0')
version = pyautogui.prompt(text='Versão nova', title='PopUp', default='5.8.1')



for i in range(int(inicio), int(fim)+1):
    funcoes.clonar_repositorio(empresas.lista[i]['nome'])

    funcoes.mudanca_versao(old_version, version)

    funcoes.mudanca_cordova()

    funcoes.remove_external()

    funcoes.build_apk(empresas.lista[i]['nome'])

    funcoes.build_bundle(empresas.lista[i]['nome'])

    funcoes.excluirRecursoJava()

    funcoes.git_commit(version, empresas.lista[i]['nome'])

    funcoes.abrir_navegador(empresas.lista[i])

# Fazer foreach, e função pra criar navegador