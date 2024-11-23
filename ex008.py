# escreva um programa que leia o valor em metros e exiba convertidos em centimetros e milimetros

mts = float(input('Digite a quantidade em metros: '))
cm = mts * 100
mm = mts * 1000

print('{} metros, equivalem a {} centimetros e {} milimetros'. format(mts,cm,mm))