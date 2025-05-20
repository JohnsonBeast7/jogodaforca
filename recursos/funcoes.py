import os, time

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def aguardar(segundos):
    time.sleep(segundos)