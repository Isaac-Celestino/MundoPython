# desenvolva um programa que leia 6 numeros inteiros, e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

pares = 0
resultado = 0

for i in range(6):
    n1 = int(input('Digite um numero: '))
    if n1 % 2 == 0:
        pares += 1
        resultado += n1
print('A quantidade de números pares que apareceram foram: {}'.format(pares))
print('O resultado da soma deles é: {}'.format(resultado))
