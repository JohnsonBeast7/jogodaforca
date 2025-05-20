
import time
from recursos.funcoes import limparTela
from recursos.funcoes import aguardar



limparTela()
nomeDesafiante = input('Nome do desafiante: ')
nomeCompetidor = input('Nome do competidor: ')
limparTela()

print('Iniciando o jogo...')
aguardar(2)
limparTela()

print('Desafiante, digite as seguintes informações:')
palavraChave = input('Palavra chave: ').lower()  
dica1 = input('Dica 1: ')
dica2 = input('Dica 2: ')
dica3 = input('Dica 3: ')
controleDicas = 0

print("Carregando...")
aguardar(2)
limparTela()

palavraEscondida = ['_'] * len(palavraChave) 
letras_usadas = []
letras_erradas = []
controleLetrasErradas = 0

while True:
    limparTela()
    print("Palavra:", ' '.join(palavraEscondida))  
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
                controleLetrasErradas += 1
                if controleLetrasErradas == 6:
                    limparTela()
                    print("Você perdeu! A palavra era:", palavraChave)
                    break
        
        aguardar(2)

        
        if '_' not in palavraEscondida:
            limparTela()
            print("Parabéns, você descobriu a palavra:", palavraChave)
            break
    

    elif opcao == "2":
        
        controleDicas += 1
        if controleDicas == 1:
            print(f"Dica 1: {dica1}")
            
            aguardar(2)
        elif controleDicas == 2:
            print(f"Dica 2: {dica2}")
            
            aguardar(2)
        elif controleDicas == 3:
            print(f"Dica 3: {dica3}")
            aguardar(2)
            
        else:
            print("Você já usou todas as dicas!")
            aguardar(2)
        
        
