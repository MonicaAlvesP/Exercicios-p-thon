"""

     Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

"""

numero = int(input("Me diga um número qualquer? "))
resultado = numero % 2

if resultado == 0:
    print(f"O número \033[1:36m{numero} é PAR")
else:
    print(f"O número \033[1:36m{numero} é IMPAR")
