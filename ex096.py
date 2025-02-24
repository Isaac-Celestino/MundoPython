def area(a,b):
    areaT = a * b
    print(f'A área de um terreno {a}m2 X {b}m2 é igual a {areaT}m2')

print('Controle de área')
print('_' * 30)
a = float(input('LARGURA(m):'))
b = float(input('COMPRIMENTO(m):'))

area(a,b)