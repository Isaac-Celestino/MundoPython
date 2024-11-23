# A confederação NAcional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
# até 9 anos: MIRIM
# até 14 anos: INFANTIL
# até 19 anos: JUNIOR
# até 20 anos: SENIOR
# acima: MASTER

from datetime import datetime

ano_atual = datetime.now().year
ano_nasc = int(input('Qual o ano de nascimento?'))
idade = ano_atual - ano_nasc

if idade <= 9:
    print('sua categoria é a mirim!')
elif (idade >9) and (idade <= 14):
    print('sua categoria é infantil!')
elif (idade > 14) and (idade <= 19):
    print('sua categoria é a junior!')
elif idade == 20:
    print('sua categoria é senior!')
else:
    print('sua cetegoria é master!')