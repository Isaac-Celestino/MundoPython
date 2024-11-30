#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

conti = "S"
lista = []
lista_par = []
lista_impar = []

while conti == "S":
    num = int(input("Digite um valor: "))
    lista.append(num)
    conti = str(input("quer continuar? [S/N]")).upper().strip()
    while conti != "N" and conti != "S":
        conti = str(input("quer continuar? [S/N]")).upper().strip()

for valor in lista:
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)
print("-=" * 40)
print(f"Os valors digitados foram: {lista}")
print(f"Os valores impares digitados foram {lista_impar}")
print(f"Os valores pares digitados foram {lista_par}")