# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. No final,
# mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista_aluno = []
quant = 0

while True:
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    quant += 1
    lista_aluno.append([nome,[nota1,nota2], media])

    conti = input("Quer continuar? [S/N]").upper().strip()

    if conti == "N":
        break

print("=-" * 30)
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
print("_" * 30)

for i, aluno in enumerate (lista_aluno):
    print(f"{i:<4}{aluno[0]:<10}{aluno[2]:>8.2f}")

print("_" * 30)

while True:
    mostra_aluno = int(input("Mostrar notas de qual aluno? (999 interrompe): "))

    if mostra_aluno == 999:
        break
    if mostra_aluno < len(lista_aluno):
        print(f"Notas de {lista_aluno[mostra_aluno][0]} são {lista_aluno[mostra_aluno][1]}")
    else:
        print("Aluno nao encontrado! ")