import random
import time


dicio = {}
print('Valores sorteados: ')
for c in range(1, 5):
    num = random.randint(0,9)
    dicio[f'jogador{c}'] = num
    print(f'    O jogador{c} tirou {num}')
    time.sleep(0.75)

dicio_ord = dict(sorted(dicio.items(), key=lambda item: item[1], reverse=True))

print('Ranking dos jogadores: ')

cont = 1
for c,v in dicio_ord.items():
    print(f'    {cont}º lugar: {c} com {v}')
    time.sleep(0.75)
    cont+= 1