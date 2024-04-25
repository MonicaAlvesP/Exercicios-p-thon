"""
    38) Escreva um programa que leia dois números inteiros e compare - os,
    mostrando na tela uma mensagem:

    - O primeiro valor é maior.
    - O segundo valor é maior.
    - Não existe valor maior, os dois são iguais.
"""

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print(f'O número \033[1:35m{num1}\033[m é maior que \033[1:35m{num2}\033[m!')
elif num1 < num2:
    print(f'O número \033[1:35m{num2}\033[m é maior que \033[1:35m{num1}\033[m!')
else:
    print(f'\033[1:35mNão existe diferença de valores, os dois são iguais!!')
