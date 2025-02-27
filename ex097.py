def ler_frase(*frases):
    for frase in frases:
        linha = "~" * len(frase)
        print(linha)
        print(frase)
        print(linha)
        print()

ler_frase("Gustavo Guanabara", "Curso de python no youtube", "Cev")