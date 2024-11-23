#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Quantos Km foram rodados?: "))
dias = int(input("Quantos dias foram alugados?: "))
valordokm = km * 0.15
valordodia = dias * 60

total = valordodia + valordokm

print("O total a ser pago é R${:.2f}!".format(total))