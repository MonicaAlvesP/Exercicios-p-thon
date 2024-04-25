"""
    53) Crie um programa que leia uma frse qualquer e diga
    se ela é um PALÍNDROMO, desconsiderando os espaços.

    EXEMPLOS:
    - Apos a sopa
    - A sacada da casa
    - A torre da derrota
    - O lobo ama o bolo
    - Anotaram a data da maratona
"""

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print("\033[1:35mTemos um palíndromo\033[m.")
else:
    print("\033[1:31mA frase não é um palíndromo\033[m!")
