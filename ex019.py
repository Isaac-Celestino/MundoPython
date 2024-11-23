#um professor quer sortear um dos seu quatros alunos, faca um programa que leia os nomes e sorteie um

import random

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

lista = (aluno1, aluno2, aluno3, aluno4)

sorteio = random.choice(lista)

print("O numero sorteado é: ", sorteio)

