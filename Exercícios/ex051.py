"""
    51) Desenvolve um programa que leia o PRIMEIRO TERMO e a RAZÃO de
    uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""

primeiro = int(input('Primeiro Termo: '))
razao = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print("{} ".format(c), end='-> ')
print("ACABOU!")
