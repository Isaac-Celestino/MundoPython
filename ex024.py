#crie um programa que leia o nome de uma cidade e diga se ela comessa ou nao com "SANTO":

cidade = str(input('Digite o nome da sua cidade: ')).title()
p = cidade.find('Santo')
if p == 0:
   print('A sua cidade começa com Santo.')
else:
   print('A sua cidade não começa com Santo.')