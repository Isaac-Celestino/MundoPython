#faca um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

n1 = int(input('digite o numero que deseja contar: '))
n2 = int(input('digite até que numero deseja que a tabuada seja feita:'))

for i in range(1, n2 + 1):
    resultado = n1 * i
    print('numero {}x{} = {}'.format(n1,i,resultado))