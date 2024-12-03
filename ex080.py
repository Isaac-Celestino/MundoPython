# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

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

