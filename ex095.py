# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = []

while True:
    print('_' * 40)

    jogador = {}
    gols = []

    jogador['nome'] = str(input('Nome do jogador: '))
    j = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    for c in range(j):
        gol = int(input(f'Quantos gols na partida {c + 1}? '))  # Ajuste no índice para começar em 1
        gols.append(gol)

    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    jogadores.append(jogador)

    conti = str(input('Quer continuar? [S/N] ')).upper().strip()
    if conti == 'N':
        break

print('-=' * 20)
print(f'{"cod":<4}{"nome":<15}{"gols":<20}{"total":<5}')
print('-' * 40)

for i, jogador in enumerate(jogadores):
    print(f'{i:<4}{jogador["nome"]:<15}{str(jogador["gols"]):<20}{jogador["total"]:<5}')

print('-' * 20)

while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if dados == 999:
        print('<< VOLTE SEMPRE >>')
        break
    elif dados < 0 or dados >= len(jogadores):
        print(f'Erro! Não existe jogador com o código {dados}. Tente novamente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[dados]["nome"]}:')
        for i, gol in enumerate(jogadores[dados]['gols']):
            print(f'   No jogo {i + 1} fez {gol} gols.')
    print('-' * 40)
