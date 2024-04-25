"""
    66) Crie um programa que leia vários números inteiros pelo teclado.
    O programa só vai parar quando o usuário digitar o valor 999, que
    é a condição de parada. No final, mostre quantos números foram digi-
    tados e qual foi a soma entre eles (desconsiderando o flag).
"""
cont = soma = 0
while True:
    numeros = int(input("Digite um valor (\033[31m999 para parar\033[m): "))
    if numeros == 999:
        break
    else:
        soma += numeros
        cont += 1
print(f"A soma dos {cont} valores foi {soma}")
