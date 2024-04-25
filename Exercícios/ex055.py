"""
    55) Faça um programa que leia o peso de cinco pessoas.
    No final, mostre qual foi o maior e qual foi o menor peso lido.
"""
maior = 0
menor = 0
# P de Pessoa
for p in range(1, 6):
    peso = float(input(f"Peso da {p}ª pessoa: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso lido foi de \033[31m{maior}Kg\033[m")
print(f"E o menor peso lido foi de \033[36m{menor}Kg\033[m")
