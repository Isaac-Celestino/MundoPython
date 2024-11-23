#le o peso de 4 pessoas, e no final fala qual foi o maior e o menor lido

pesos = []
for c in range(0, 4):
    peso = float(input('Digite o peso:'))
    pesos.append(peso)

print('O menor peso é {:.2f}:'.format(min(pesos)))
print('O maior peso é {:.2f}:'.format(max(pesos)))

