#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar

reais = float(input("Quantos reais deseja converter?"))
taxadecambio = float(5.07)
dolar = reais / taxadecambio

print("R${:.2f} sao equivalentes a U${:.2f}".format(reais,dolar))