#faca um programa que leia um numero inteiro, seu atecessor, e seu sucessor

n = int(input('digite um numero inteiro: '))
ant = n - 1
suc = n + 1

print('o sucessor do numero {} será o numero {}, e o antecessor será o numero {}. '.format(n,suc,ant))
#Outra forma de se fazer seria retirar as variaveis suc e ant, e adcionar as equaccoes diretamente no format
# exemplo: format(n,n+1,n-1))