"""

    Escreva um programa que leia a velocidade de um carro.

    ° Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
    ° A multa vai custar R$7.00 por cada Km acima do limite.

"""

velocidade = float(input('Insira a velocidade do veiculo em km: '))
velocidade_max = 80
multa = 7
velocidade_total = velocidade - velocidade_max
valor_multa = velocidade_total * multa

if velocidade > velocidade_max:
    print(f'Seu veiculo foi multado em R$\033[7:30:44m{valor_multa}\033[m')
else:
    print('Esta tudo OK!')
