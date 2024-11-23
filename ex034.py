#escreva um programa que leia o salario de um funcionari e calcule o valor do seu aumento, para salarios superiores a R$1250,00
# calcule um aumento de 10%, para inferiores ou iguais o aumento sera de 15%

salario = float(input('Digite o sálario: '))

if salario > 1250.00:
    salario1 = (salario + (salario / 100 * 10))
    print("Seu salario novo é {:.2f}".format(salario1))
else:
    salario2 = salario + (salario / 100 * 15)
    print('Seu salario novo é {:.2f}'.format(salario2))