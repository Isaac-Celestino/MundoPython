#faça um programa que calcule a soma entre todos os numeros impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for i in range(0,501):
    if i % 3 == 0 and i % 2 != 0:
        cont = cont + 1
        soma = soma + i
print('A soma de todos os {} numeros impares divididos por 3 são: {}'.format(cont,soma))
