#le a idade de 7 pessoas, e fala quantas atingiram a maior idade
maiorIdade = 0
menorIdade = 0

for c in range(0,7):

    idade = int(input('Digite sua idade:'))

    if int(idade) >= 21:
        maiorIdade = maiorIdade + 1
    else:
        menorIdade = menorIdade + 1

print(menorIdade,'sao menores de idade e ', maiorIdade, 'sao maiores de idade')