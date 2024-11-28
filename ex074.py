import random

num1 = random.randint(0, 10)
num2 = random.randint(0, 10)
num3 = random.randint(0, 10)
num4 = random.randint(0, 10)
num5 = random.randint(0, 10)

lista = (num1, num2, num3, num4, num5)

print(f"Os numeros sortedos foram: {lista}")

print("O menor valor sorteado foi:", min(lista))
print("O maior valor sorteado foi:", max(lista))
