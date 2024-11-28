from itertools import count

times = ("Botafogo", "Palmeiras", "Internacional", "Fortaleza", "Flamengo",
    "São Paulo", "Cruzeiro", "Bahia", "Corinthians", "Atlético-MG",
    "Vasco", "Vitória", "Juventude", "Athletico-PR", "Grêmio", "Fluminense",
    "Criciúma", "Bragantino", "Cuiabá", "Atlético-GO")

print("=-" * 40)
print("A lista do brasileirao: ", times)
print("=-" * 40)
print("Os 5 primeiros colocados sao: ", times[0:4])
print("=-" * 40)
print("Os 4 ultimos colocados sao: ", times[-4:])
print("=-" * 40)
print("Em ordem alfabetica: ", sorted(times))
print("=-" * 40)

pos_juve = (times.index("Juventude"))

print(f"O Juventude está em {pos_juve + 1}º posicao!")