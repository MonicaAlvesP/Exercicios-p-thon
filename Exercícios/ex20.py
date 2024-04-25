"""

    O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
    Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

"""
from random import shuffle
a1 = str(input("Primeiro Aluno: "))
a2 = str(input("Segundo Aluno: "))
a3 = str(input("Terceiro Aluno: "))
a4 = str(input("Quarto Aluno: "))
lista = [a1, a2, a3, a4]
shuffle(lista)

print(f"A ordem de apresentações será:")
print(f'\033[7:40m{lista}')
