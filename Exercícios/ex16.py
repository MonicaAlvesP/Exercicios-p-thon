"""

    Crie um programa que leia um número Real qualquer pelo teclado e mostre na Tela a sua porção inteira.

EX:
Digite um número: 6.127
O número 6.127 tem a parte inteira 6.

"""

from math import floor

num = float(input("Digite um número: "))
print(f"O número \033[34m{num}\033[m tem a parte inteira \033[34m{floor(num)}\033[m")
