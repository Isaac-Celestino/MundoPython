#desenvolva um programa que leia o nome, idade, sexo de 4 pessoas e no final mostra: a media de  idade do grupo, o nome
#do homem mais velho, quantas mulheres tem menos de 20

for c in range (1,5):
    print('--- {}ª --- '.format(c))
    nome = str(input('nome: '))
    idade = int(input('idade: '))
    sexo = str(input('sexo: [M/F]: ')).upper()




'''mulheres20 = 0
homem_mais_velho = {"nome": "", "idade": 0}

for _ in range(1,5):

    print('-'*4, "{}ª pessoa".format(_), '-'*4 )
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo? [M/F]: ').strip().upper()

    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    elif sexo == 'M' and idade > homem_mais_velho["idade"]:
        homem_mais_velho = {"nome": nome, "idade": idade}

print(f"Quantidade de mulheres com menos de 20 anos: {mulheres20}")
if homem_mais_velho["nome"]:
    print(f"O homem mais velho é {homem_mais_velho['nome']} com {homem_mais_velho['idade']} anos.")
else:
    print("Nenhum homem foi cadastrado.")'''


