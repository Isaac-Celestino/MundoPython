#Crie um programa que leia varios numeros inteiros pelo teclado. No final da execucao, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuários se ele quer ou nao continuar a digitar valores.

lista = []

numero = int(input("Digite um numero: "))
lista.append(numero)
cont = 1

continuar = "Y"
while continuar != "N":
    continuar = str(input("Deseja continuar? [S/N]")).upper()
    cont += 1
    if continuar == "N":
        break
    else:
        numero = int(input(f"Digite o {cont}º numero: "))
        lista.append(numero)

media = sum(lista) / len(lista)

print(f"O menor numero digitado foi {min(lista)}")
print(f"O maior numero digitado foi {max(lista)}")
print("A media dos numeros digitados {:.2f}".format(media))