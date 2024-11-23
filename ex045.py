# crie um programa que faça o computador jogar jokenpô com você.

import random

print('Vamos brincar de jokenpô:')
escolha = input('Escolha entre pedra, papel e tesoura: ')
print('Você escolheu {}'.format(escolha))
lista = ('tesoura','pedra','papel')
maq = random.choice(lista)

if maq == "tesoura" and escolha == 'papel':
    print("você perdeu... a màquina escolheu tesoura!")
elif maq == "tesoura" and escolha == 'pedra':
    print('Você ganhou!!! a máquina escolheu tesoura!')
elif maq == 'pedra' and escolha == 'papel':
    print('Você ganhou!!! a máquina escolheu pedra!')
elif maq == 'pedra' and escolha == 'tesoura':
    print('Você perdeu... a máquina escolheu pedra!')
elif maq == 'papel' and escolha == 'tesoura':
    print('Você ganhou!!! a máquina escolheu papel!')
elif maq =='papel' and escolha == 'pedra':
    print('Você perdeu... a máquina escolheu papel!')
else:
    print('Você empataram!')
