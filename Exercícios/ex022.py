"""

    Crie um programa que leia o nome completo de uma pessoa e mostre:

    - O nome com todas as letras maiúsculas
    - O nome com todas minúsculas
    - Quantas letras ao td (sem considerar espaços).
    - Quantas letras tem o primeiro nome.

"""

nome = str(input("Digite seu nome Completo: ")).strip()
n1 = nome.split()
n2 = nome.replace(' ', '')
print("Analisando seu nome...")
print(f'Seu nome em maiúsculas  \033[1:34m{nome.upper()}\033[m')
print(f'Seu nome em minúsculas  \033[1:34m{nome.lower()}\033[m')
print(f'Seu nome tem ao todo \033[1:36m{len(n2)}\033[m '
      f'letras sem considerar espaços')  # outra solução é usar len() - count(' ')

print(f"\033[7:30:46m Seu primeiro nome é {n1[0]} e ele tem {len(n1[0])} letras")
