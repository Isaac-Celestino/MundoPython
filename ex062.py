    #62) Melhore o Desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.


resp = str(input("Deseja calcular alguma PA: [S/N]")).upper()
while resp == "S":
    primeiro_termo = int(input("Qual número você deseja iniciar: "))
    razao = int(input('Qual o valor da razão: '))

    contadorTermos = 1  # Contador para os 10 termos da PA.
    progressao = 10  # Número de termos da progressão.

    while contadorTermos <= progressao:
        termo = primeiro_termo + (contadorTermos - 1) * razao  # Fórmula do termo geral da PA.
        print(f"Termo {contadorTermos}: {termo}")
        contadorTermos += 1
        print("-"*40)

    resp = str(input("Deseja continuar Calculando outra PA: [S/N]")).upper()

print("Fim de calculo.")