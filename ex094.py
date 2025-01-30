# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

pessoas = []
mulher_lista = []

while True:
    dicio = {}
    dicio['nome'] = str(input('Nome: '))
    dicio['sexo'] = str(input('Sexo: [F/M] ')).upper().strip()
    dicio['idade'] = int(input('idade: '))

    if dicio['sexo'] == 'F':
        mulher_lista.append(dicio['nome'])

    pessoas.append(dicio)

    conti = input('Quer continuar? [S/N]').upper().strip()
    if conti == 'N':
        break
print("-=" * 30)

soma_idades = sum(pessoa['idade'] for pessoa in pessoas)
media_idade =  soma_idades / (len(pessoas))

print(f'-- O grupo tem {len(pessoas)} pessoas.')
print(f'-- O grupo tem em média {media_idade:.2f} anos.')

if mulher_lista:
    nomes_formatados = " e ".join(mulher_lista)
    print(f"--Nome das mulheres cadastradas: {nomes_formatados}")
else:
    print("--Nenhuma mulher foi cadastrada.")

acima = [pessoa for pessoa in pessoas if pessoa['idade'] > media_idade]

if acima:
    print("\n--As pessoas com idade acima da média são:")
    for pessoa in acima:
        print(f"nome = {pessoa['nome']}; sexo = {pessoa['sexo']}; idade = {pessoa['idade']};\n")

else:
    print("\nNenhuma pessoa tem idade acima da média.")