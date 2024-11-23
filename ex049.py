# refaça o exercicio do desfio 009, mostrando a tabuada de um número que usuário escolher, só que agora utilizando o laço for

num = int(input('Digite o numero que deseja a tabuada: '))

for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))