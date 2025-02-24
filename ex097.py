def ler_frase(*frases):
    for frase in frases:
        linha = "~" * len(frase)
        print(linha)
        print(frase)
        print(linha)
        print()

ler_frase("Python é incrível!", "Automatizando tarefas", "Criando scripts eficientes")