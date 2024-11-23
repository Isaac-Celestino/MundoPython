#faca um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra "A"
#em que posicao ela aparece a primeira vez
#em que posicao ela aparece e ultima vez

frase = input("Digite uma frase: ")

frasePronta = frase.lower()

print('O numero de letras a é: ',frasePronta.count("a"))

print('a letra aparece primeiramente na localizacao:',frasePronta.find("a"))

print('A letra aparece a ultima vez em: ', frasePronta.rfind("a"))
