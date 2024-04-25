"""
    68) Faça um programa que jogue par ou impar com o computador.
    O jogo só será interrompido quando o jogador PERDER, mostrando
    o total de vitórias consecutivas que ele conquistou no final do Jogo.
"""
from random import randint
print('\033[34m''°' * 50)
print(" VAMOS JOGAR PAR OU IMPAR ")
print('°' * 50, '\033[m')

contador = 0

while True:
    pc = randint(0, 10)
    valor = int(input("Digite um valor: "))
    escolha = str(input("Par ou Impar? [P/I] ")).upper()
    print('\033[34m''°''\033[m' * 50)
    soma = valor + pc
    if escolha == 'I' and soma % 2 != 0:
        print("Você VENCEU!")
        contador += 1
        print("Vamos jogar novamente...")
    elif escolha == 'P' and soma % 2 == 0:
        print("Você VENCEU!")
        contador += 1
        print("Vamos jogar novamente...")
    else:
        print("Você PERDEU!")
        print(f"Você jogou {valor} e o computador {pc}. Total de {soma} ", end='')
        print('DEU PAR.' if soma % 2 == 0 else 'DEU IMPAR.')
        break
    print(f"Você jogou {valor} e o computador {pc}. Total de {soma} ", end='')
    print('DEU PAR.' if soma % 2 == 0 else 'DEU IMPAR.')
    print('\033[34m''°''\033[m' * 50)
print(f"GAME OVER! Você venceu {contador} vezes.")

