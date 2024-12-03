matriz = [[0,0,0],[0,0,0],[0,0,0]]
num_par = []

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input("Digite um valor: "))
        if matriz[l][c] % 2 == 0:
            num_par.append(matriz[l][c])

print("-=" * 30)
for l in range (0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end='')
    print()
print("-=" * 30)
terceira_coluna = [matriz[l][2] for l in range(3)]
segunda_linha = [matriz[1][c] for c in range(3)]

print(f"A soma dos valores pares é {sum(num_par)}")
print("A soma dos valores da terceira coluna é ",terceira_coluna)
print(f"O maior valor da segunda linha é {max(segunda_linha)}")