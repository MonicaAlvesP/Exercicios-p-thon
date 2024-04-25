"""
    51) Faça um programa que mostre na tela uma contagem regressiva para a estoura
    de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre
    eles.

"""
from time import sleep

# Substitui o número 0 pela queima de fogos
for i in range(10, -0, -1):
    print(i)
    sleep(1)
print("\033[1:33mBOOM BOOM POOW\033[m")
