"""
    61) Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
    mostrando os 10 primeiros termos da progressão usando a estrutura
    WHILE.
"""
from time import sleep

print("\033[35mGerador de PA\033[m")
print('=-=' * 10)

primeiro = int(input('Primeiro Termo: '))
razao = int(input("Razão da PA: "))
contador = 1
termo = primeiro

while contador <= 10:
    print(f"\033[35m{termo}\033[m -> ", end='')
    sleep(1)
    termo += razao
    contador += 1
print("FIM!")
