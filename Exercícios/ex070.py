"""
    70) Crie um programa que leia o nome e o preço de vários produtos.
    O programa deverá perguntar se o usuário vai continuar.
    No final, mostre:

    A) Qual é o total gasto na compra.
    B) Quantos produtos custam mais de R$ 1000.
    C) Qual é o nome do produto mais barato.
"""
total_gasto = 0
produtos_caros = 0
nome_doproduto_barato = 0
preco_produto_barato = 0
print("=" * 36)
print(" \033[34m *****\033[m Armarinhos Dorneles  \033[34m*****\033[m")
print("=" * 36)

while True:
    produto = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$"))
    if produto >= 1000:
        produtos_caros += 1
    else:
        nome_doproduto_barato = produto
        preco_produto_barato = preco
    total_gasto = produtos_caros + nome_doproduto_barato
    continuar = str(input("Deseja continuar: [S/N] ")).upper()
    if continuar == "N":
        break
print("-" * 9, "FIM DO PROGRAMA", "-" * 9)
print(f"O total da compra foi R${total_gasto:.2f}")
print(f"Temos {produtos_caros} produtos custando mais de R$1.000.00")
print(f"O produto mais barato foi {nome_doproduto_barato} que custa {}")
