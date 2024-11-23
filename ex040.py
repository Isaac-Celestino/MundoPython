# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média antigida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print("você está reprovada, sua nota é {}.".format(media))
elif (media > 5) and (media < 6.9):
    print('você está de recuperação, sua nota é {}, estude mais!'.format(media))
else:
    print('você está aprovado, sua nota é {}, Boas Férias!'.format(media))