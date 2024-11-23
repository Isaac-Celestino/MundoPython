#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c= float(input("informe a temperatura em °C: "))
F = 1.8 * c + 32

print("A temperatura  em {}°C equivale a {:.2f}°F!".format(c,F))

