# desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média

nome= input('digite o nome do aluno: ')
nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
media = (nota1 + nota2) / 2

print('a media do {} é igual a {:.2f}'.format(nome,media))
