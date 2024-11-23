#faca um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o ultimo nome separadamente

nome = input("Qual o seu nome completo? ")

primeiroNome = nome.split()[0]
ultimoNome = nome.split()[-1]

print("O primeiro nome é: ", primeiroNome)
print("O ultimo nome é: ", ultimoNome)

