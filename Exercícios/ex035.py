"""

   CHEFÂO FINAL DO MUNDO 1!

    Desenvolva um programa que leia o comprimento de três rotas
    e diga ao úsuario se elas podem ou não formar um triângulo.

"""
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
    print('\033[1:34m Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('\033[1:34mOs segmentos acima NÃO PODEM FORMAR um triângulo!')
