import time

def contagem():
    print("-=" * 30)
    init = 0
    print('CONTAGEM DE 1 A 10 DE 1 EM 1:')
    while init < 10:
        init += 1
        print(init,' ', end='')
        time.sleep(0.25)
    print('FIM!')

    print("-=" * 30)
    print('CONTAGEM DE 10 ATÉ 0 DE 2 EM 2:')
    init = 10
    while init >= 0:
        print(init, ' ', end='')
        init -= 2
        time.sleep(0.25)
    print('FIM!')
    print("-=" * 30)
    print('Agora é a sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    if passo == 0:
        print("O passo não pode ser zero!")
        return

    if inicio < fim:
        if passo < 0:
            print("O passo deve ser positivo para uma contagem crescente!")
            return
        while inicio <= fim:
            print(inicio, ' ', end='')
            inicio += passo
            time.sleep(0.25)
    else:
        if passo > 0:
            print("O passo deve ser negativo para uma contagem regressiva!")
            return
        while inicio >= fim:
            print(inicio, ' ', end='')
            inicio += passo  # passo é negativo
            time.sleep(0.25)
    print('FIM!')
    print("-=" * 30)

contagem()