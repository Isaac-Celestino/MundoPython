
from datetime import datetime

dicio = {}

ano_atual = datetime.now().year
dicio['nome'] = str(input('Nome: '))
ano_nasc= int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasc
dicio['idade'] = idade

dicio['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))

if dicio['ctps'] != 0:
    dicio['contratacao'] = int(input('Ano de contratação: '))
    dicio['salario'] = float(input('Salário: R$ '))
    ano_apos = dicio['contratacao'] + 35
    idade_apos = ano_apos - ano_nasc
    dicio['ano_aposentadoria'] = ano_apos
    dicio['idade_aposentadoria'] = idade_apos

print('=-' * 30)
print(f'O nome tem o valor {dicio['nome']}')
print(f'Idade tem o valor {dicio['idade']}')
print(f'CTPS tem o valor {dicio['ctps']}')
if dicio['ctps'] != 0:
    print(f'contratacao tem o valor {dicio['contratacao']}')
    print(f'salario tem o valor {dicio['salario']}')
    print(f'Aposentadoria tem o valor{dicio['idade_aposentadoria']}')
print(dicio)