lista = []
peso_maior = 0
peso_menor = float("inf")
contpe = 0

while True:
    nome = str(input("Nome: "))
    peso = int(input("Peso: "))

    lista.append([nome, peso])
    contpe += 1
    peso_maior = max(peso_maior, peso)
    peso_menor = min(peso_menor, peso)

    if input("Quer continuar? [S/N] ").strip().upper() == "N":
        break

nomes_maior = [p[0] for p in lista if p[1] == peso_maior]
nomes_menor = [p[0] for p in lista if p[1] == peso_menor]

print("-=" * 40)
print(f"Ao todo, voce cadastrou {contpe} pessoas. ")
print(f"O maior peso foi {peso_maior}Kg. Peso de {' e '.join(nomes_maior)}.")
print(f"O menor peso foi {peso_menor}Kg. Peso de {' e '.join(nomes_menor)}.")