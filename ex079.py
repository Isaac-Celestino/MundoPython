
lista = []
conti = "S"
while conti == "S":
    num = int(input("Digite um valor: "))
    if num in lista:
        print(f"Valor duplicado, nao vou adicionar...")
    else:
        lista.append(num)
    conti = str(input("Deseja continuar? [S/N] ")).upper().strip()

print("=-" * 40)
print(f"Voce digitou os valores {sorted(lista)}")
