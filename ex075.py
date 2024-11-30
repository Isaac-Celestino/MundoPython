# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

num = (int(input("Digite um número: ")),
       int(input("Digite um número: ")),
       int(input("Digite um número: ")),
       int(input("Digite um número: ")))

print(f"Voce digitou os valores {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 in num:
       print(f"O valor 3 apareceu na {num.index(3)} posicao")
else:
       print("O valor 3 nao foi digitado em nenhuma posicao")
print(f"Os valores pares digitados foram ", end=" ")
for n in num:
       if n % 2 == 0:
              print(n, end=" ")