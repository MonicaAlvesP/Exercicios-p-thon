"""
    60) Faça um programa que leia um número qualquer e mostre o seu FATORIAL.

        EX:
        5!= 5x4x3x2x1 = 120

    Fazer usando WHILE e FOR!
"""
# Feito com o modulo Factorial da lib math
# 4 linha e já está resolvido, mas precisamos mostrar como é feito o calculo

"""from math import factorial

num = int(input("Digite um número para calcular seu Fatorial: "))
f = factorial(num)
print(f"O fatorial de {num} é {f}")"""

numero = int(input("Digite um número para calcular seu Fatorial: "))
contador = numero
fatorial = 1
print(f"\033[32mCalculando {numero}!\033[m ... ", end='')

while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(f'\033[32m{fatorial}\033[m')