import time

def maior_cont(a):
    print('=-' * 30)
    print('Analisando os valores passados...')

    if not a:
        print("Nenhum valor foi informado.")

    print(*a, 'Foram informados',len(a),'valores ao todo')

    b = max(a)

    print(f'O maior valor informado foi {b}')

num = (20,12,9,21,42)
num1 = (0,)
maior_cont(num)
maior_cont(num1)