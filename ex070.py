print("_" * 30)
print("      Loja Super Baratao")
print("_" * 30)
total = []
cont = "S"
maiorQue1000 = 0
barato = float("inf")
nome_do_mais_barato = ""
while cont == "S":
    nome_do_produto = str(input("Nome do produto:"))
    preco = float(input("preco: R$"))
    if preco > 1000:
        maiorQue1000 += 1
    total.append(preco)
    if preco < barato:
        barato = preco
        nome_do_mais_barato = nome_do_produto
    cont = str(input("Deseja continuar? [S/N]")).upper().strip()[0]
    while cont != "S" and cont != "N":
        cont = str(input("Deseja continuar? [S/N]")).upper().strip()[0]
    valorTotal = sum(total)

print("_" * 7,"FIM DO PROGRAMA", "_" * 7)
print(f"O valor total da compra deu {valorTotal}!")
print(f"Temos {maiorQue1000} produtos custando mais que R$1000!")
print(f"O produto mais barato foi {nome_do_mais_barato} custando {min(total)}")
