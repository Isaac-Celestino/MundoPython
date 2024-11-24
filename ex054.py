#le o ano de nascimento de 7 pessoas, e fala quantas atingiram a maior idade

import datetime
atual = datetime.date.today().year
totMaior = 0
totMenor = 0

for pess in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    menor = 18 -idade

    if idade >= 18:
        print('voce tem {} anos, voce é maior de idade. '.format(idade))
        totMaior += 1
    else:
        print('ainda faltam {} anos para voce ser maior de idade. '.format(menor))
        totMenor += 1

print('{} pessoas maiores de idade'.format(totMaior))
print('{} pessoas menores de idade'.format(totMenor))