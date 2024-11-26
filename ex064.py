#crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condicao de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (Desconsiderando o flag)

numero = int(input("Digite um numero:"))

lista = []
resultado = 0
quant = 0
while numero != 999:
    if numero != 999:
        lista.append(numero)
        numero = int(input("Digite um numero:"))
        resultado = sum(lista)
        quant = len(lista)

print(f"A soma de todos os numeros digitados é {resultado}")
print(f"Foram necessarios {quant} numeros.")