"""
    50) Desenvolva um programa que leia seis números inteiros e mostre
    a soma apenas daqueles que forem PARES. Se o valor digitado for IMPAR, descomsidere - o.
"""
soma = 0

# Verificando se o número digitado é PAR
for c in range(6):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        # Adicionando valor a variavel soma
        soma += numero

print(f"A soma dos números pares é: {soma}")

'''
Solução do Teacher Guanabara

soma = 0
cont = 0

for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma deles foi {}'.format(cont, soma))
'''
