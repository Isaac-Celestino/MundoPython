#faca um programa que leia a altura e a largura de uma parede em metros
#calcule a sua area e a quantidade de tinta necessaria para pintala
#sabendo que cada litro de tinta pinta 2m quadrados

Altura = float(input("Qual a altura da parede que deseja pintar? "))
Largura = float(input("Qual a largura da parede? "))

mtsQuadrados = Altura * Largura
Tinta = mtsQuadrados / 2

print("Serao necessarios {:.1f} litros de tinta para pintar {} m² de área. ".format(Tinta,mtsQuadrados))