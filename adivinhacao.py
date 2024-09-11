import random

def jogar():

    print("*" *50)
    print("Bem vindo ao jogo de adivinhaçõa!")
    print("*" *50)

    numero_secreto = random.randrange(1, 101)
    total_tentativa = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print(" (1) fácil (2) Médio (3) Dificil")

    nivel = int(input("Define o nivel:"))

    if(nivel == 1):
        total_tentativa = 20
    elif(nivel == 2):
        total_tentativa = 10
    else:
        total_tentativa = 5

    for rodada in range(1, total_tentativa + 1):
        print("Tentativa {} de {}" .format(rodada, total_tentativa))
        chute = int(input("Digite um numero entre 1 e 100: "))
        print("Você digitou ", chute) 

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        acertou = numero_secreto==chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                    print("vc errou! o seu chute foi maior que o numero secreto")
            elif(menor):
                    print("vc errou! o seu chute foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)      
            pontos = pontos - pontos_perdidos   

    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()