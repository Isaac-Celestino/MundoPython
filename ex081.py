conti = "S"
lista = []

while conti == "S":
    num = int(input("Digite um valor: "))
    lista.append(num)
    conti = str(input("Quer continuar? [S/N]")).upper().strip()
    while conti != "S" and conti != "N":
        conti = str(input("Quer continuar? [S/N]")).upper().strip()
print(f"foram digitados {len(lista)} elementos")
print("Os valores decrescente ",lista)
if 5 in lista:
    print("O valor 5 foi digitado")
else:
    print("O valor 5 nao foi digitado")