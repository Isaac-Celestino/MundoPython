#faca um algoritmo que leia o salario de um funcionario e mostre com 15% de aumento

salario = float(input("Qual o salario do funcionario? "))
aumento = float((salario / 100) * 20)
salarionovo = salario + aumento

print("O salario novo do funcionario será {:.2f}".format(salarionovo))