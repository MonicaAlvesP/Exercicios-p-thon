"""

    Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

"""
from datetime import date

ano = int(input("Que ano você quer analisar? Coloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano \033[1:34m{ano} é BISSEXTO!\033[m")
else:
    print(f"O ano \033[1:34m{ano} NÂO é BISSEXTO!\033[m")
