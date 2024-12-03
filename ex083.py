# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expre = str(input("Digite uma expressao: "))
paren_expre = 0

for char in expre:
    if char == "(":
        paren_expre += 1
    elif char == ")":
        paren_expre -= 1

if paren_expre % 2 == 0:
    print("é uma expressao valida")
else:
    print("Nao é uma expressao valida")

