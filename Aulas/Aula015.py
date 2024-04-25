"""cont = 1
while cont <= 10:
    print(f'{cont}-> ', end='')
    cont += 1
print('FIM')"""

"""n = s = 0
while n != 999:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
print(f"A soma vale {s}!")
"""

nome = "Bernardo"
idade = 1
print(f"O {nome} tem {idade} de idade!") # versão fstring usada a partir da versão 3.6+
print("O {} tem {} anos de idade!".format(nome, idade)) # usada na versão PYTHON 3
print("O %s tem %d anos de idade!" % (nome, idade)) # usada na versão PYTHON 2
