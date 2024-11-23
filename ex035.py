#desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo

reta1 = float(input('Digite a medida da primeira reta: '))
reta2 = float(input('Digite a medida da segunda reta: '))
reta3 = float(input('Digite a medida da terceira reta: '))

if reta1 < (reta2 + reta3):
    if reta2 < (reta1 + reta3):
        if reta3 < (reta2 + reta1):
            print('é possível formar um triângulo')
        else:
            print('Não é possível formar um triângulo')
    else:
        print('Não é possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')