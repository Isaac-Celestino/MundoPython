#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

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
