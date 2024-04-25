"""

    Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

"""

nome = str(input("Qual é o seu nome Completo: ")).strip()
s = 'silva' in nome.lower()
print(f"Seu nome tem Silva? \033[7:30:44m{s}\033[m")
