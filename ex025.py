#Crie um programa que leia o nome de uma pessoa e diga se ela tem silva no nome

nome =input('Qual o seu nome completo: ')

achar = nome.find('Silva')

if achar == (-1):
    print("voce nao tem Silva no nome!")
else:
    print('Tem Silva no nome e comeca na posicao: ', achar)

