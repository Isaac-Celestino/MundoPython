# desenvolva um programa que leia o primeiro termo de uma PA (progressão aritmética, exemplo: 1 até 100, pulando de 10 a 10). no final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input("Qual número você deseja iniciar: "))
razao = int(input('Qual o valor da razão: '))

# Calcula e exibe os 10 primeiros termos da PA
for i in range(10):
    termo = primeiro_termo + i * razao
    print(termo)
