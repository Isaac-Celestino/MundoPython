# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior. os dois são iguais

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input('Digite o segundo numero: '))

if numero1 > numero2:
    print('{} é maior que {}'.format(numero1,numero2))
elif numero2 > numero1:
    print('{} é maior que {}'.format(numero2,numero1))
else:
    print('Os dois números são iguais.')