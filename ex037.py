# escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base da conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal


numero = int(input('Digite o número que deseja converter: '))

print('opção 1 = binário')
print('opção 2 = octal')
print('opção 3 = hexadecimal')

escolha = int(input('qual das opções acima deseja converter: '))

if escolha == 1:
    print(bin(numero)[2:])
elif escolha == 2:
    print(oct(numero)[2:])
elif escolha == 3:
    print(hex(numero)[2:])
else:
    print ('Essa não é uma opção válida')
