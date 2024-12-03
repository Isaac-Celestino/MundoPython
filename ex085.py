valores = list()
valores_impar = list()
valores_par = list()

for c in range(1,8):
    numero = int(input(f"Digite o {c}º valor: "))
    valores.append(numero)

for v in valores:
    if v % 2 == 0:
        valores_par.append(v)
    else:
        valores_impar.append(v)


print('=-' * 30)
print(f'Os valores pares digitados foram {valores_par}')
print(f'Os valores impares digitados foram {valores_impar}')