#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

continu = "S"
while continu == "S":
    numero_por_extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
                          'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

    numero = int(input("Digite um numero entre 0 e 20: "))

    if numero >= 0 and numero <=20:
        print(f"voce digitou ", numero_por_extenso[numero])
    else:
        while numero > 20:
            numero = int(input("tente novamente...Digite um numero entre 0 ae 20: "))
        while numero <0:
            numero = int(input("tente novamente...Digite um numero entre 0 ae 20: "))

        print(f"voce digitou", numero_por_extenso[numero])
    print("=" * 40)
    continu = str(input("Quer continuar?")).upper()
    print("=" * 40)

print("FIM")