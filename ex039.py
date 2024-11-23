# faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# se já passou do tempo do alistamento
# seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo

from datetime import datetime

anoDeNasc = int(input('Qual ano você nasceu: '))
ano_atual = datetime.now().year
idade = int(ano_atual - anoDeNasc)
tempoQuePassou = int((ano_atual - anoDeNasc) - 18)
tempoQueFalta = int(18 - (ano_atual - anoDeNasc))

if idade == 18:
    print('esse ano você fará {}'.format(idade))
    print('Caso não tenha se alistado, lembre se de ir!')
elif idade > 18:
    print('Esse ano você fara {}'.format(idade))
    print('já se passaram {} ano da idade correta para o alistamente, deve ir imediamente!'. format(tempoQuePassou))
else:
    print('esse ano você fará {}'.format(idade))
    print('Não será necessario se alistar!')
    print('Ainda faltam {} ano/anos, recomendo ir se preparando.'.format(tempoQueFalta))