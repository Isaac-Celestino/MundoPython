#faca um pr0grama que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

import math

catetoAdjacente = float(input("Digite o cateto adjacente:"))
catetoOposto = float(input("Digite o cateto oposto:"))

hipotenusa = math.hypot(catetoOposto, catetoAdjacente)

print("é {:.2f}".format(hipotenusa))
