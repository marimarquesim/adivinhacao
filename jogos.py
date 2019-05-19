import forca
import adivinhacao

print("*********************************")
print("Escolha o seu jogo!")
print("*********************************")

print("(1) FORCA (2)ADIVINHAÇÃO")

jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("Jogando forca")
    forca.jogar_forca()
elif(jogo == 2):
    print("Jogando adivinhação")
    adivinhacao.jogar_adivinhacao()