# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("=" * 35)
print(" " * 10, "Banco CEV")
print("=" * 35)

valor = int(input("Que valor voce quer sacar? R$"))
divisao50 = valor // 50
valor %= 50
divisao20 = valor // 20
valor %= 20
divisao10 = valor // 10
valor %= 10
divisao1 = valor // 1

print(f"Total de {divisao50} cedulas de 50 reais")
print(f"Total de {divisao20} cedulas de 20 reais")
print(f"Total de {divisao10} cedulas de 10 reais")
print(f"Total de {divisao10} cedulas de 1 real")

print("=" * 35)
print("Volte sempre ao BANCO CEV! Tenha um bom dia!")


