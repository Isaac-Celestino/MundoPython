#faca um programa que leia o seno, cosseno e tangente de um numero

import math

numero = float(input("Digite o numero que deseja calcular: "))

angulo_em_radianos = math.radians(numero)

seno = math.sin(angulo_em_radianos)
cosseno = math.cos(angulo_em_radianos)
tangente = math.tan(angulo_em_radianos)

print("resultado é igual a Seno: {:.4f}, Cosseno: {:.4f}, Tangente: {:.4f}.".format(seno,cosseno,tangente))