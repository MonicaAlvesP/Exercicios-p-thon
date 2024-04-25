"""
    64) Crie um programa que leia vários números inteiros pelo
    teclado. O programa só vai parar quando o usuário digitar o valor 999,
    que é a condição de parada. No final, mostre quantos números foram
    digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
print('-' * 60)
# todas as variaveis receberam o mesmo valor, então podemos unifica - las
cont = soma = 0
num = int(input(" Digite um número [\033[1:31m999 para parar\033[m]: "))

while num != 999:
    soma += num
    cont += 1
    num = int(input(" Digite um número [\033[1:31m999 para parar\033[m]: "))

print('-' * 60)
print(f' Você digitou {cont} números e a soma entre eles foi {soma}.')
