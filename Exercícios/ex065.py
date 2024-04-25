"""
    65) Crie um programa que leia vários números inteiros pelo teclado. No
    final da execução, mostre a média entre todas os valores a qual foi o
    maior e o menor valor lido. O programa deve perguntar ao usuário se
    ele quer ou não continuar a digitar valores.
"""
resposta = 'S'
soma = quantidade = media = maior = menor = 0
while resposta in 'S':
    num = int(input("Digite um número: "))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
print('-' * 43)
media = soma / quantidade
print(f" Você digitou {quantidade} números e a média foi {media:.2f}")
print(f" Maior valor foi {maior} e o menor valor {menor}!")
print('-' * 43)
