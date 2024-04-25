"""
    44) Elabore um programa que calcule o valor a ser pago
    por um produto, considerando o seu preço normal e condição
    de pagamento:

    - Á vista dinheiro/cheque: 10% de desconto.
    - Á vista no cartão: 5% de desconto.
    - Em até 2x no cartão: preço normal.
    - 3x ou mais no cartão: 20% de juros.
"""
# Coletando preço do produto
print("{:=^40}".format(' Lojas Moça Chique '))
preco = float(input('Informe o preço do produto: R$'))

# Definindo a condição de pagamento
print('Escolha como deseja pagar:')
print('\033[1:35m1\033[m- Á vista dinheiro/cheque')
print('\033[1:35m2\033[m- À vista no cartão')
print('\033[1:35m3\033[m- Em até 2x no cartão')
print('\033[1:35m4\033[m- Em até 3x ou mais no cartão')
condicao_pagamento = int(input('Sua opção: '))

# Desinindo preço do produto
if condicao_pagamento == 1:
    preco_final = preco * 0.9
    print(f'O valor a ser pago é de: \033[1:35mR${preco_final:.2f}\033[m (com 10% de desconto!)')
elif condicao_pagamento == 2:
    preco_final = preco * 0.95
    print(f'O valor a ser pago é de: \033[1:35mR${preco:.2f}\033[m (com 5% de desconto!)')
elif condicao_pagamento == 3:
    preco_final = preco / 2
    print(f'O valor parcelado em 2x: \033[1:35mR${preco_final:.2f}\033[m')
elif condicao_pagamento == 4:
    preco_final = preco * 1.2
    quantidade_de_parcelas = int(input('Digite o número de parcelas desejado: '))
    valor_da_parcela = preco_final / quantidade_de_parcelas
    print(
        f'O valor a ser pago é: \033[1:35m{quantidade_de_parcelas}\033[m '
        f'parcelas de \033[1:35mR${valor_da_parcela:.2f}\033[m '
        f'(total: \033[1:35mR${preco_final:.2f})\033[m (juros de 20%)')
else:
    print('\033[1:31mOpção Ínvalida!\033[m')
