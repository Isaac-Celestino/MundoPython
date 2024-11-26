# 61) refaca o desafio 51, lendo o primeiro termo e a razao de uma PA. mostrando os 10 primeiros termos da progressao usando a estrutura while.

primeiro_termo = int(input("Qual número você deseja iniciar: "))
razao = int(input('Qual o valor da razão: '))

contadorTermos = 1  # Contador para os 10 termos da PA.
progressao = 10  # Número de termos da progressão.

while contadorTermos <= progressao:
    termo = primeiro_termo + (contadorTermos - 1) * razao  # Fórmula do termo geral da PA.
    print(f"Termo {contadorTermos}: {termo}")
    contadorTermos += 1
print('FIM!')