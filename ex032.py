#faça um programa que leia um ano qualquer e mostre se ele é bissexto:

ano = int(input('Digite um ano:'))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('é um ano bissexto!!')
        else:
            print('Não é um ano bissexto...')
    else:
        print('é um ano bissexto!')
else:
    print('Não é um ano bissexto...')
