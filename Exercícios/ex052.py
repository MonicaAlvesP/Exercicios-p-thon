"""
    52) Faça um programa que leia um númerointeiro e
    diga se ele é ou não um número primo.
"""
num = int(input("Digite um número: "))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print(f'\n\033[mO nuḿero {num} foi divísivel {tot} vezes')

if tot == 2:
    print('E por isso ele é \033[34mPRIMO!\033[m')
else:
    print('E por isso ele \033[31mNÂO È PRIMO!\033[m')
