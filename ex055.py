#le o peso de 4 pessoas, e no final fala qual foi o maior e o menor lido

maior = 0
menor = 0

for p in range (1,6):
    peso = float(input("Digite o peso da {}ª pessoal: ".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))

''' pesos = []
for c in range(1, 5):
    peso = float(input('Digite o peso da {}ª:'.format(c)))
    pesos.append(peso)

print('O menor peso é {:.1f}kg.'.format(min(pesos)))
print('O maior peso é {:.1f}kg.'.format(max(pesos)))'''

