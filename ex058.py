#melhore o jogo DESAFIO 028 onde o computador vai pensar em um numero entre 0 a 10. Só que agora o jogador vai tentar adicinhar até acertar. mostrando no final quantos palpites foram necessários para vencer.

import random

numero = int(input('Digite um numero de 0 a 10: '))

lista = 0,1,2,3,4,5,6,7,8,9,10

sorteio = random.choice(lista)

while numero != sorteio:
    numero = int(input('Digite um numero de 0 a 10: '))

print("Parabéns!!! voce acertou, o numero era {}".format(numero))