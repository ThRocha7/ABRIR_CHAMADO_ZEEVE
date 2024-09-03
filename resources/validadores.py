from pyautogui import press, hotkey, write
import pyperclip as clip
from time import sleep

PAUSE = .8

def conferir_arq(nome:str) -> bool:
    copia = clip.paste()

    if copia == nome:
        print('valido')
        press(['enter', 'enter'])
        return True
    else: 
        looping = looping_tentativa(nome)
        if looping == True:
            print('valido')
        else:
            print('Não encontrei')
        return looping
    

def looping_tentativa(nome:str) -> bool:
    parar_while = False
    anterior = ''

    while parar_while != True:
        press(['enter', 'down', 'f2'])
        hotkey('ctrl', 'c')
        copia_while = clip.paste()

        if copia_while == nome:
            press(['enter', 'enter'])
            parar_while = True
            return True
        if anterior == copia_while:
            parar_while = True
            return False
        
        anterior = copia_while


def procurar_pdf(nome_arq, direct):
    press(['f4'])
    hotkey('ctrl', 'a')
    clip.copy(direct)
    hotkey('ctrl', 'v')
    press('enter')
    sleep(1)
    press('tab')
    sleep(1)
    write(nome_arq)
    sleep(5)
    press(['tab', 'tab', 'tab', 'down', 'up', 'f2'])
    hotkey('ctrl', 'c')
    validado = conferir_arq(nome_arq)
    return validado

def formatar_agencia(agencia:str)->str:
    if len(agencia) <= 4:
        if len(agencia) == 1:
            agencia = '000' + agencia
            return agencia
        elif len(agencia) == 2:
            agencia = '00' + agencia
            return agencia
        elif len(agencia) == 3:
            agencia = '0' + agencia
            return agencia
        else:
            return agencia
    else:
        print('agencia invalida')