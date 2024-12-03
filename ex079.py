# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

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
