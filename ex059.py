'''59) crie um programa que leia dois valores e mostre uma mensagem na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operacao solicitado em cada caso'''

opcao = 0
numero1, numero2 = 0, 0

while opcao != 5:
    if opcao == 4 or opcao == 0:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))

    print("""
O que você deseja fazer:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
""")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        resultado = numero1 + numero2
        print(f"O resultado da soma é: {resultado}")
    elif opcao == 2:
        resultado = numero1 * numero2
        print(f"O resultado da multiplicação é: {resultado}")
    elif opcao == 3:
        if numero1 > numero2:
            print("O primeiro número é maior!")
        elif numero1 < numero2:
            print("O segundo número é maior!")
        else:
            print("Os números são iguais!")
    elif opcao == 4:
        print("Informe novos números.")  # Volta ao início do loop
    elif opcao == 5:
        print("Obrigado por usar nosso programa!")
    else:
        print("Opção inválida! Tente novamente.")

    print("-" * 60)
