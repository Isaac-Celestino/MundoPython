# escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o sálario do comprador e em quantos anos ele vai pagar
# calcule o valor da prestação  sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

import math

print('Olá, iremos analisar a sua situação para um empréstimo imobiliário:')

casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário: '))
anos = int(input('Em quantos anos você irá pagar: '))

if casa == 0 or salario == 0:
    print('Não é possível solicitar a análise caso o valor da casa ou o salário sejam igual a zero.')
else:
    meses = anos * 12
    parcela = casa / meses
    limite = salario * 30 / 100

    if parcela > limite:
        print('Seu empréstimo será negado no momento...')
    else:
        print('Meus parabéns! Seu empréstimo foi aprovado! A parcela será no valor de {:.2f} durante {} meses.'.format(parcela, meses))

