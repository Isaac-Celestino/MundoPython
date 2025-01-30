# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dicio = {}
gols = []

dicio['nome'] = str(input('Nome do jogador: '))
j = int(input(f"Quantas partidas {dicio['nome']} jogou?"))
c = 0

while c != j:
    gol = int(input(f'Quantos gols na partida {c}?'))
    gols.append(gol)
    c += 1
    if c == j:
        break

total = sum(gols)

dicio['gols'] = gols
dicio['total'] = total

print('-=' * 30)
print(dicio)
print('-=' * 30)
print(f'O campo nome tem o valor {dicio['nome']}.')
print(f'O campo gols tem o valor {dicio['gols']}.')
print(f'O campo total tem o valor {dicio['total']}.')
print('-=' * 30)
print(f'O jogador {dicio['nome']} jogou {j} partidas.')

c = 0
while c < j:
    print(f'    => Na partida {c + 1}, fez {dicio['gols'][c]} gols.')
    c += 1

print(f'Foi um total de {total} gols.')