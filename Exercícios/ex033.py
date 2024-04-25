"""

    Faça um programa que leia três números mostre qual é o MAIOR e qual é o MENOR.

"""

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

# Checking who is the smallest
smaller = a
if b < c and b < a:
    smaller = b
if c < a and c < b:
    smaller = c
# Checking who is the greatest
bigger = a
if b > c and b > a:
    bigger = b
if c > a and c > b:
    bigger = c
print(f"O menor valor digitado foi \033[1:34m{smaller}\033[m")
print(f"O maior velor digitado foi \033[1:34m{bigger}\033[m")
