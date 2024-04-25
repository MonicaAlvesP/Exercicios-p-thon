"""

Escreva um programa que leia um valor em metros e o exiba convertido em centimetros a milimetros.

"""

medida = float(input('Digite a distância em metros: '))
cm = medida * 100
mm = medida * 1000
print(f'A medida de \033[1:34m{medida}\033[mm '
      f'corresponde a \033[1:34m{cm:.0f}\033[mcm, '
      f'e em milimetros é \033[1:34m{mm:.0f}\033[mmm ')
