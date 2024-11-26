# 60) faca um programa que leia um numero qualquer e mostre o seu fatorial.
#
# Ex: 5! = 5x4x3x2x1 = 120
#
# de preferencia faca com while e com for

'''Maneira de fazer com While'''
print("Vamos calcular um fatorial.")

numero = int(input("Digite o numero que deseja calcular o fatorial:"))
cont = 1
fatorial = 1

while cont <= numero:
    fatorial *= cont
    cont += 1

print(fatorial)

'''Maneira de fazer com for'''
numero = int(input("Digite o numero que deseja calcular o fatorial:"))
fatorial = 1

for c in range (numero, 0, -1):
    fatorial *= c

print(fatorial)