# faca um algoritmo que leia um preco de um produto e mostre o seu novo preco com 5% de desconto

preco = float(input("Qual o preco original do produto? "))
desconto = float((preco / 100) * 5)
preconovo = preco - desconto

print("O valor do produto com o desconto é {:.2f}".format(preconovo))