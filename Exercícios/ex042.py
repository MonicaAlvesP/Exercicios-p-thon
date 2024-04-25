"""
    42) Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
    que tipo de triângulo será formado:

    - EQUILÁTERO: todos os lados iguais.
    - ISÓSCELES: dois lados iguais.
    - ESCALENO: todos os lados diferentes.
"""
# Coletando os valores
print('Analisador de Triângulos..')
print('-='*20)
a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if (a + b < c) or (a + c < b) or (b + c < a):
    print('\033[1:30:41mNÂO É UM TRIÂNGULO!\033[m')
elif (a == b) and (a == c):
    print(f'\033[1:35mEQUILÁTERO\033[m: todos os lados iguais!')
elif (a == b) or (a == c) or (b == c):
    print(f'\033[1:35mISÓSCELES\033[m: dois lados iguais!')
else:
    print(f'\033[1:35mESCALENO\033[m: todos os lados diferentes!')
