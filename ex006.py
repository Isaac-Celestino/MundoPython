#crie um algoitmo que leia seu numero e mostre seu dobro, triplo e raiz quadrada

import math

n1 = int(input('digite um numero inteiro: '))
dobro = n1 * 2
triplo = n1 * 3
raizquadrada = math.sqrt(n1)

print('O dobro do numero {} é {}.\nSeu triplo {}.\nSua raiz quadrada {:.2f}'.format(n1, dobro, triplo,raizquadrada))

#outra formula para raiz quadrada seria raizquadrada = ** (1/2)
