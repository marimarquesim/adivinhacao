import random

def jogar_adivinhacao():

    print("*********************************")
    print("Bem vindo no jogo de adivinhação!")
    print("*********************************")

    numero_secreto = round(random.random() * 100) #gera um número entre o.o e 1.o
    total_de_tentativas = 3
    pontos = 1000

    print("Qual o nível de dificuldade?", numero_secreto)
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas + 1):
        print("Tentativa {} de {}". format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número entre 1 e 100: ")
        chute = int(chute_str)
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        print("Você digitou", chute_str)

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto")
            elif(chute < numero_secreto):
                print("Você errou! O seu chute foi menor que o número secreto")
                pontos_perdidos = abs(chute - numero_secreto)
                pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if(__name__=="__main__"):
    jogar_adivinhacao()