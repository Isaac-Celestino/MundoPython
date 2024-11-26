

lista = []
n = int(input("Digite um numero:"))
lista.append(n)


while n != 999:
        n = int(input("Digite um numero:"))
        if n != 999:
            lista.append(n)

resultado = sum(lista)
print(lista)
print(resultado)