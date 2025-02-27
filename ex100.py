import random

def sort():
    list_num = []
    while len(list_num) < 5:
        num = random.randint(1, 10)
        list_num.append(num)
    return list_num

def Soma_par(lista):
    som_n = 0
    for num in lista:
        if num % 2 == 0:
            som_n += num
    return som_n

result = sort()

print('Sorteando 5 valores da lista:', *result, 'PRONTO!')

soma_pares = Soma_par(result)
print(f'A soma dos números pares de {result}, temos {soma_pares}')