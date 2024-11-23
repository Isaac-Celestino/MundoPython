#desenvolva um programa que leia o nome, idade, sexo de 4 pessoas e no final mostra: a media de  idade do grupo, o nome
#do homem mais velho, quantas mulheres tem menos de 20

mulheres20 = 0
homem_mais_velho = {"nome": "", "idade": 0}

for _ in range(2):  # Loop de 0 a 1
    nome = input('Digite seu nome: ')
    idade = int(input('Digite a sua idade: '))
    sexo = input('Digite o seu sexo? [M/F]: ').strip().upper()

    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    elif sexo == 'M' and idade > homem_mais_velho["idade"]:
        homem_mais_velho = {"nome": nome, "idade": idade}

# Exibindo os resultados
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres20}")
if homem_mais_velho["nome"]:
    print(f"O homem mais velho é {homem_mais_velho['nome']} com {homem_mais_velho['idade']} anos.")
else:
    print("Nenhum homem foi cadastrado.")


