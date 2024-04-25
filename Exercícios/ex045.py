"""
    45) Cire um programa qeu faça o computador jogar JOKENPÔ com você.
"""
from random import randint
from time import sleep

itens = ['PEDRA', 'PAPEL', 'TESOURA']
print('''Suas opções:
[0] PEDRA
[1} PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))

print('Jo')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('\033[35m-=\033[m' * 12)
computador = randint(0, 2)

print(f'Computador jogou \033[36m{itens[computador]}\033[m')
print(f'Jogador jogou \033[33m{itens[jogador]}\033[m')
print('\033[35m-=\033[m' * 12)

if computador == 0:       # COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('\033[31mEMPATOU\033[m')
    elif jogador == 1:
        print('\033[33mJOGADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[36mCOMPUTADOR VENCE\033[m')
    else:
        print('\033[31mJOGADA ÍNVALIDA!\033[m')

elif computador == 1:     # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('\033[36mCOMPUTADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[31mEMPATOU\033[m')
    elif jogador == 2:
        print('\033[33mJOGADOR VENCE\033[m')
    else:
        print('\033[31mJOGADA ÍNVALIDA!\033[m')

elif computador == 2:     # COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('\033[33mJOGADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[36mCOMPUTADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[31mEMPATOU\033[m')
    else:
        print('\033[31mJOGADA ÍNVALIDA!\033[m')
