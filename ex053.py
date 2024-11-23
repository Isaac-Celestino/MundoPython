#polindromo

nome = input('Digite a palavra ou frase: ')

frase = nome.replace(" ", "").lower()

fraseContraria = frase[::-1]

if frase == fraseContraria:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")