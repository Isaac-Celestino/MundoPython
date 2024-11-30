# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


lista = []

for c in range(0,5):
    n = input(f"Digite um valor na posicao {c}: ")
    lista.append(n)

print(f"Voce digitou os valores {lista}")

maior = max(lista)
menor = min(lista)

posicao_maior = []
posicao_menor = []

for cont in range(len(lista)):
    if lista[cont] == maior:
        posicao_maior.append(str(cont))
    if lista[cont] == menor:
        posicao_menor.append(str(cont))

print(f"O maior valor é {maior} e está na posição {'... '.join(posicao_maior)}.")
print(f"O menor valor digitado foi {menor} na posicao {'... '.join(posicao_menor)}.")
