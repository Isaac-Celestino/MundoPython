#o mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalho dos alunos.
# faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

lista = (aluno1, aluno2, aluno3, aluno4)

ordem_sorteada = random.sample(lista, len(lista))

print("Ordem de apresentação dos alunos:")
for i, aluno in enumerate(ordem_sorteada, start=1):
        print(f"{i}. {aluno}")
