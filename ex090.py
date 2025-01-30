# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

dic = {'nome': str(input('Nome: '))}

dic['media'] = float(input(f'Média do {dic['nome']}: '))

print(f'Nome é igual a {dic['nome']}')
print(f'Média é igual a {dic['media']}')

if dic['media'] < 7:
    print('Situacao igual a reprovado')
else:
    print('Situacao igual a aprovado')