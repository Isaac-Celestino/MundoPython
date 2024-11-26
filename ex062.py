    #62) Melhore o Desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.


'''resp = str(input("Deseja calcular alguma PA: [S/N]")).upper()
while resp == "S":
    primeiro_termo = int(input("Qual número você deseja iniciar: "))
    razao = int(input('Qual o valor da razão: '))

    contadorTermos = 1
    progressao = 10

    while contadorTermos <= progressao:
        termo = primeiro_termo + (contadorTermos - 1) * razao
        print(f"Termo {contadorTermos}: {termo}")
        contadorTermos += 1
        print("-"*40)

    resp = str(input("Deseja continuar Calculando outra PA: [S/N]")).upper()

print("Fim de calculo.")'''

resp = str(input("Deseja calcular alguma PA? [S/N] ")).upper()

while resp == "S":
    primeiro_termo = int(input("Qual número você deseja iniciar: "))
    razao = int(input('Qual o valor da razão: '))

    contador_termos = 1
    termos_mostrados = 10  # Quantidade inicial de termos a serem mostrados
    total_termos = 0       # Total de termos mostrados ao longo do programa

    while termos_mostrados != 0:
        total_termos += termos_mostrados
        while contador_termos <= total_termos:
            termo = primeiro_termo + (contador_termos - 1) * razao
            print(f"Termo {contador_termos}: {termo}")
            contador_termos += 1
        print("-" * 40)
        termos_mostrados = int(input("Quantos termos você deseja mostrar a mais? [Digite 0 para encerrar]: "))

    print("Encerrando esta progressão aritmética.")
    resp = str(input("Deseja calcular outra PA? [S/N] ")).upper()

print("Fim do cálculo.")
