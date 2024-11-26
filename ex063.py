#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequencia de fibonacci.

#ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

n = int(input("Qual o valor limite que deseja calcular: "))

termo1 = 0
termo2 = 1
cont = 3

while cont <= n:
    termo3 = termo1 + termo2
    print(termo3)

    termo1 = termo2
    termo2 = termo3
    cont += 1

print("FIM")