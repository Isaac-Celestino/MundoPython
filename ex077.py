# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

# Vogais que queremos verificar
vogais = "AEIOU"

# Loop para ler as palavras e mostrar as vogais presentes
for palavra in palavras:
    encontrados = ""  # String para armazenar as vogais encontradas
    for vogal in vogais:
        if vogal in palavra:
            encontrados += vogal  # Concatenando as vogais encontradas
    # Exibindo a palavra e as vogais encontradas
    print(f"Na palavra '{palavra}' temos {', '.join(encontrados)}")
