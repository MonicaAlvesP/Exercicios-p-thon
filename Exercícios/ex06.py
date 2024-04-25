"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

"""

num = int(input('Digite um número: '))
m = num * 2
t = num * 3
r = num ** 0.5
print(f'Seu número é \033[1:35m{num}\033[m')
print(f'O dobro de \033[1:35m{num}\033[m vale \033[1:35m{m}\033[m')
print(f'O triplo de \033[1:35m{num}\033[m vale \033[1:35m{t}\033[m')
print(f'A raiz quadrada de \033[1:35m{num}\033[m é igaul a \033[1:35m{r:.2f}\033[m')
