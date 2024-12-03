import random
import time

print("_" * 30)
print("JOGA NA MEGA SENA".center(30))
print("_" * 30)
jogos = int(input('Quantos jogos voce quer que eu sorteie? '))
cont = 1
sorteio = []

print(f"-=-=-= SORTEANDO {jogos} JOGOS  -=-=-=")

while cont < jogos + 1 :
    print(f"Jogo {cont}:", end='')
    sorteio = [ random.randint(1, 60) for _ in range(6)]
    print(sorteio)
    cont += 1
    time.sleep(1)

print("-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=")