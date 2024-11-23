# escreva um programa que faça o computador pensar em um numero inteiro de 0 a 5
#e peça para o usuario tentar adivinhar qual foi o numero escolhido pelo computador
# o computador deverá escrever na tela se o usuario acertou ou não

import random

numero = int(input('Digite um numero de 0 a 5: '))

lista = 0,1,2,3,4,5

sorteio = random.choice(lista)

print('O número sorteado foi ',sorteio)

if numero == sorteio:
    print('Você acertou o numero!')
else:
    print('Você não acertou...')