

valor = 1

while valor > 0:
    c = 0
    print("_" * 30)
    valor = int(input("Quer ver a tabuada de qual valor? "))
    print("_" * 30)
    while c < 10:
        if valor >= 0:
            c += 1
            resultado = valor * c
            print(f"{valor} x {c} = {resultado}")
        else:
            print("PROGRAMA TABUADA ENCERRADO. volte sempre!")
            break
