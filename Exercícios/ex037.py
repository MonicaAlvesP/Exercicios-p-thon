"""
    Escreva um programa que leia um número inteiro qualquer
    e peça para o uruário escolher qual será a base de conversão:

    ° 1 para binário
    ° 2 para octal
    ° 3 para hexadecimal
"""
# Recebendo o número inteiro
num = int(input("Informe um número inteiro: "))

# Recebdno a opção de conversão
print('\033[7:33mEscolha uma opção de conversão:\033[m')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')

opcao = int(input('Sua opção: '))

# Verificando a opção escolhida e realizando a conversão
if opcao == 1:
    print('Binário:', bin(num)[2:])
elif opcao == 2:
    print("Octal:", oct(num)[2:])
elif opcao == 3:
    print('Hexadecimal:', hex(num)[2:])
else:
    print("\033[1:31mOpção inválida!\033[m")
