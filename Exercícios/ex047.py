"""
    Crie um programa que mostre na tela todos os números pares
    que estão no intervalo entre 1 e 50.
"""
from time import sleep

# Minha solução
print('\033[37mNúmeros pares entre 1 e 50\033[36m')
for i in range(2, 51, 2):
    print(i)
    sleep(0.5)
print('\033[37mFIM!\033[m')

# Solução do Professor Guanabara
'''
for n in range(2, 51, 2):
    print(n, end=" ")
print('ACABOU')

'''
