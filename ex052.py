# faça um programa que leia um número inteiro e diga se ele é ou não um número primo


print('Vamos descobrir se um numero é primo!!!')
numero = int(input('Qual numero deseja saber:'))

if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print(numero, 'não é primo')
            break
    else:
        print(numero, 'é primo')
elif numero == 0:
    print(numero, 'é zero')
elif numero == 1:
    print(numero, 'é um')
else:
    print(numero, 'é negativo')
