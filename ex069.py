
homens = 0
mais18 = 0
cont = "S"
mulher20 = 0

while cont == "S":
    print("_" * 30)
    print("      CADASTRE UMA PESSOA       ")
    print("_" * 30)
    idade = int(input("Idade: "))
    if idade > 18:
        mais18 +=1
    sexo = input("Sexo: [M/F]").upper().strip()[0]
    while sexo != "M" and sexo != "F":
        sexo = input("Sexo: [M/F]").upper().strip()[0]
    if sexo == "F" and idade < 20:
        mulher20 += mulher20 + 1
    elif sexo == "M":
        homens += 1
    else:
        break
    print("_" * 30)
    cont = str(input("Deseja continuar? [S/N]")).upper().strip()[0]
    while cont != "S" and cont != "N":
        cont = str(input("Deseja continuar? [S/N]")).upper().strip()[0]

print(f"Tem {mais18} homens com mais de 18 anos!")
print(f"Tem {homens} homens cadastrados!")
print(f"Tem {mulher20} mulheres com menos de 20 anos!")
