"""

    Escreva um programa que faça o computador 'pensar' em um número
    inteiro entre 0 e 5 e peça para o úsuario tentar descobrir qual foi
    o número escolhido pelo computador.

    O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""
from random import randint

num = randint(0, 5)
usuario = int(input('Adivinhe o número entre 0 e 5: '))

if num == usuario:
    print("\033[7:30:44m Você Ganhou!")
else:
    print("O computador ganhou! \033[m")

print(f"O número escolhido foi \033[1:36m{num}")
