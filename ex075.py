tupla = ()
contnove = 0
numpar = 0

while len(tupla) < 5:
    num = int(input("Digite um valor:"))
    tupla = tupla + (num,)

    if num == 9:
        contnove = contnove + 1
    elif num % 2 == 0:
        numpar = numpar + 1

print(f"Voce digitou os valores: {tupla}")
print(f"O numero 9 apareceu {contnove} vezes!")
if 3 not in tupla:
    print("O valor 3 nao foi digitado em nenhuma posicao.")
else:
    print(f"O numero 3 apareceu na {(tupla.index(3) + 1)}ª posicao ")
print(f"Foram digitados {numpar} numeros pares")