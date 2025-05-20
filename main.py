import os
import time

# Entradas iniciais
os.system('cls')
nomeDesafiante = input('Nome do desafiante: ')
nomeCompetidor = input('Nome do competidor: ')
os.system('cls')

print('Iniciando o jogo...')
time.sleep(2)
os.system('cls')

print('Desafiante, digite as seguintes informações:')
palavraChave = input('Palavra chave: ').lower()  # força minúscula
dica1 = input('Dica 1: ')
dica2 = input('Dica 2: ')
dica3 = input('Dica 3: ')
controleDicas = 0

print("Carregando...")
time.sleep(2)
os.system('cls')

palavraEscondida = ['_'] * len(palavraChave)  # usamos lista aqui!
letras_usadas = []
letras_erradas = []

while True:
    os.system('cls')
    print("Palavra:", ' '.join(palavraEscondida))  # junta com espaços
    print("Letras já usadas:", ', '.join(letras_usadas))
    print("(1) Jogar")
    print("(2) Solicitar Dica")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        letra = input("Digite uma letra: ").lower()

        if letra in letras_usadas:
            print("Você já tentou essa letra!")
        else:
            letras_usadas.append(letra)

            if letra in palavraChave:
                print("Acertou!")
                for i in range(len(palavraChave)):
                    if palavraChave[i] == letra:
                        palavraEscondida[i] = letra
            else:
                print("Errou!")
        
        time.sleep(2)

        
        if '_' not in palavraEscondida:
            os.system('cls')
            print("Parabéns, você descobriu a palavra:", palavraChave)
            break
    

    elif opcao == "2":
        
        controleDicas += 1
        if controleDicas == 1:
            print(f"Dica 1: {dica1}")
            
            time.sleep(2)
        elif controleDicas == 2:
            print(f"Dica 2: {dica2}")
            
            time.sleep(2)
        elif controleDicas == 3:
            print(f"Dica 3: {dica3}")
            time.sleep(2)
            
        else:
            print("Você já usou todas as dicas!")
            time.sleep(2)
        
        
