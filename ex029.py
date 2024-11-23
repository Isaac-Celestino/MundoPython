#escreva um programa que leia a velocidade de um carro,
#se ele ultrapassar 80 km mostre uma mensagem dizendo que ele foi multado
#a multa vai custar 7 reias por cada km acima do limite

km = int(input("A quantos km/h o carro estava?"))
multa = (km - 80) * 7

if km <= 80:
    print("estava dentro do limite de velocidade.")
else:
    print("estava acima do limite de velocidade, a multa é o valor de: {:.2f} reais!".format(multa))