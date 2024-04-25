"""

    Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

"""

valor_inicial = float(input('Digite o valor do produto: '))
valor_do_desconto = valor_inicial * 5 / 100
valor_final = valor_inicial - valor_do_desconto
print(f'O valor do produto é R$\033[1:36m{valor_inicial:.2f}\033[m, com 5% de desconto o valor será R$\033[1:36m{valor_final:.2f}\033[m')


# A partir desse desafio eu decidi não colocar variáveis abreviadas
# Isso facilita o entendimento, e deixa o codigo mais limpo