#desenvolva um programa que pergunte a distancia de uma viagem em km
#calcule o preço da passagem, cobrando R$ 0,50 por km rodado até 200 km
# e R$ 0,45 por viagems mais longas


kms = int(input("Quantos kms você pretende viajar?"))

if kms <= 200:
    custo1 = kms * 1/2
    print('Sua viagem custará: {:.2f}'.format(custo1))
else:
    custo2 = kms * 0.45
    print('Sua viagem custará: ',custo2)
















