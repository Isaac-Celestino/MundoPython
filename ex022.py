#crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letra maiuscculas,
# o nome com todas as letras minusculas,
# quantas letras ao total(sem contar os espacos)
#  quantas letras tem o primeiro nome

nomeCompleto = str(input("Olá, qual o seu nome completo?"))

nomeMaiusculo = nomeCompleto.upper()
print ("O seu nome em maiusculo é",nomeMaiusculo)

nomeMinusculo = nomeCompleto.lower()
print ("O seu nome em minusculo é",nomeMinusculo)

nomeSemEspaco = nomeCompleto.replace(" ", "")
quantidadeDeLetras = len(nomeSemEspaco)
print('A quantidade de letras é',quantidadeDeLetras)

nomeSeparado = nomeCompleto.split()[0]
print("o primeiro nome é",nomeSeparado)

letrasPrimeiroNome = len(nomeSeparado)
print("A quantidade de letras do primeiro nome é", letrasPrimeiroNome)
