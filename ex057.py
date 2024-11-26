#faca um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peca a digitacao novamente até um valor correto.
sexo = str(input("Digite o seu sexo: [M/F]")).strip().upper()[0]

while sexo != 'M' and sexo!='F':
    sexo = str(input("Digite um valor valido: [M/F]")).upper()[0]

print("Seu sexo foi cadastrado com sucesso!")
print(sexo)