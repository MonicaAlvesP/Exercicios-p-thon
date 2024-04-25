"""

    Faça um programa que leia uma frase pelo teclado e mostre:

        - Quantas vezes aparece a letra "A".
        - Em que posição ela aparece a primeira vez.
        - Em que posição ela aparece a última vez.

"""

frase = str(input("Digite uma frase: ")).upper().strip()
print(f"A letra A aparece \033[7:30:44m{frase.count('A')} vezes na frase.\033[m")
print(f"A primeira letra A apareceu naposição \033[7:30:44m{frase.find('A') + 1}\033[m")
print(f"A última letra A apareceu na posição \033[7:30:44m{frase.rfind('A') + 1}\033[m")
