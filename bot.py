import pyautogui
import funcoes
import empresas
import os

# Pausa
pyautogui.PAUSE = 0.5 #Pausa Geral

# Run
rodando = False
lista = 'Lista de aplicativos: \n'

root = os.getcwd()

for empresa in empresas.lista:
    lista = lista + empresa['nome']+"\n"

inicio = pyautogui.prompt(text=lista, title='Início', default='')
fim = pyautogui.prompt(text=lista, title='Fim', default='')

old_version = pyautogui.prompt(text='Versão antiga', title='PopUp', default='5.8.2')
version = pyautogui.prompt(text='Versão nova', title='PopUp', default='5.8.3')


for empresa in empresas.lista:
    
    if(inicio == empresa['nome']):
        rodando = True
    
    if(rodando):
        funcoes.clonar_repositorio(empresa['nome'], root)

        funcoes.mudanca_versao(old_version, version)

        funcoes.conf_cordova()

        funcoes.remove_external()

        funcoes.build_apk(empresa['nome'])

        funcoes.build_bundle(empresa['nome'])

        funcoes.excluirRecursoJava()

        funcoes.git_commit(version, empresa['nome'])

        funcoes.abrir_navegador(empresa, root)
        
    if(fim == empresa['nome']):
        rodando = False
    

# Fazer foreach, e função pra criar navegador