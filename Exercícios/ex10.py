"""

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

CONSIDERE
{US$1.00 = R$5.21

"""
valor_em_reais = float(input("Quanto você tem na carteira? R$"))
valor_em_dolar = valor_em_reais / 5.23
print(f"Com R$\033[1:31m{valor_em_reais}\033[m você pode comprar US$\033[1:31m{valor_em_dolar:.2f}")
