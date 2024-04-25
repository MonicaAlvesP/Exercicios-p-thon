"""

    Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
    e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
    que o carro custa R$60 por dia e R$0.15 por Km rodado.

"""

dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
pagar = (dias * 60) + (km * 0.15)
aluguel_por_dia = 60 * dias
aluguel_por_km = 0.15 * km
tot_pagar = aluguel_por_dia + aluguel_por_km

print(f"O total a pagar é de R$\033[34m{tot_pagar:.2f}\033[m")
