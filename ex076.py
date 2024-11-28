# Tupla contendo pares de (nome, preço)
itens = (
    ("Pao", 1),
    ("Borracha", 2.00),
    ("Caderno", 15.90),
    ("Estojo", 25.0),
    ("Transferidor", 4.2),
    ("Compasso", 9.99),
    ("Mochila", 120.32),
    ("Canetas", 22.30),
    ("Livros", 34.9)
)

# Cabeçalho
print("_" * 40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("_" * 40)

# Iterando sobre a tupla
for nome, valor in itens:
    print(f"{nome:.<30} R$ {valor:.2f}")
print("_" * 40)

