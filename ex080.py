lista = []

for _ in range(5):
    num = int(input("Digite um valor: "))

    pos = 0
    while pos < len(lista) and num > lista[pos]:
        pos+=1
    lista.insert(pos, num)
    print(f"O valor foi adicionado na posicao {pos}")

print("=-" * 40)
print(f"Os valores adicionados em ordem foram: {lista}")

