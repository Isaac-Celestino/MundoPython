#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

print("=-" * 20)
print("VAMOS JOGAR PAR OU IMPAR:")
print("=-" * 20)

escolha = 0
resultado = 0
contvit = 0
while escolha == resultado:
    n = int(input("Diga um valor: "))

    escolha = (input("Par ou Impar? [P/I]")).upper()
    if escolha == "P":
        escolha = "Par"
    else:
        escolha = "Impar"

    n_pc = random.randint(1,50)

    if (n_pc + n) % 2 == 0:
        resultado = "Par"
    else:
        resultado = "Impar"

    print(f"Voce jogou {n} e o computador {n_pc}. Total deu {resultado}!")
    print("-" * 40)

    if escolha == resultado:
        print("Voce Venceu!")
        print("Vamos jogar novamente...")
        contvit += 1
        print("-" * 40)
    else:
        print("Voce perdeu...")
        print("=-" * 20)

print(f"GAME OVER! voce venceu {contvit} vezes.")