# refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilatero: todos ps lados iguais
# isosceles: dois lados iguais
# escaleno: todos os lados diferentes

reta1 = float(input('Digite a medida da primeira reta: '))
reta2 = float(input('Digite a medida da segunda reta: '))
reta3 = float(input('Digite a medida da terceira reta: '))

if reta1 < (reta2 + reta3):
    if reta2 < (reta1 + reta3):
        if reta3 < (reta2 + reta1):
            print('é possível formar um triângulo')
            if (reta1 == reta2) and (reta1 == reta3):
                print('Você tem um triângulo equilatero!')
            elif (reta1 == reta2) and reta1 != reta3 or (reta1 == reta3) and (reta1 != reta2):
                print('você tem um triângulo isoscele!')
            else:
                print('você tem um triângulo escaleno')
        else:
            print('Não é possível formar um triângulo')
    else:
        print('Não é possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')
