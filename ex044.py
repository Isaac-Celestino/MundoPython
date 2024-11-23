# elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# a vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format('LOJA DO ISAAC'))

produto = float(input('Qual o valor das compras?'))

print('A seguir as formas de pagamento: ')
print('[1] a vista dinheiro/cheque: 10% de desconto')
print('[2] À vista no cartão: 5% de desconto')
print('[3] em até 2x no cartão: preço normal')
print('[4] 3x ou mais no cartão: 20% de juros')

forma = int(input("Qual será a forma de pagamento? "))

if forma == 1:
    resultado = produto - (produto / 10)
    print('Seu produto custará {}'.format(resultado))
elif forma == 2:
    resultado = produto - (produto / 20)
    print('Seu produto custará {}'.format(resultado))
elif forma == 3:
    print('Seu produto custará {}'.format(produto))
elif forma == 4:
    resultado = produto + (produto / 5)
    print('Seu produto custará {}'.format(resultado))
else:
    print('Não é uma opção válida!')