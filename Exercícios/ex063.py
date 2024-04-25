"""
    63) Escreva um programa que leia N inteiro qualquer e mostre na tela
    o N primeiros elementos de uma Sequência de Fibonacci.

        EX:
        0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""
print('-' * 24)
print("\033[1:36m Sequência de Fibonacci \033[m")
print('-' * 24)

n = int(input("Quantos termos você quer mostrar? "))
print('_' * 24)
t1 = 0
t2 = 1
print(f"\033[1:34m {t1} -> {t2}\033[m", end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'\033[1:34m -> {t3}\033[m', end='')
    t1 = t2
    t2 = t3
    cont += 1
print("\033[1:36m -> FIM.. \033[m")
print('-' * 24)