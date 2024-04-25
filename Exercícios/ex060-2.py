# Exercício feito com o laço FOR

numero = int(input("\033[32mDigite um número para calcular seu\033[m \033[35mFatorial\033[m: "))
fatorial = 1

for c in range(1, numero + 1):
    fatorial *= c
    print(c, "\033[35m! = \033[m", fatorial)

print(f'\033[35mO fatorial de\033[m \033[32m{numero}\033[m \033[35mé\033[m \033[32m{fatorial}\033[m')
