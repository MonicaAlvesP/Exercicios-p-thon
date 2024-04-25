"""
    59) Crie um programa que leia dois valores e mostre um menu na tela:

    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA

    Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0
maior_num = 0

while opcao != 5:
    print('=-=' * 10)

    print("""[1] Somar
[2] Multiplicar
[3] Maior e Menor
[4] Adicionar novos números
[5] Sair do programa""")
    opcao = int(input("\033[1:34m>>>> Qual é a sua opção: \033[m"))

    print('=-=' * 10)
    if opcao == 1:
        soma = n1 + n2
        print(f"\033[7:34mA soma de {n1} + {n2} é {soma}\033[m")
    elif opcao == 2:
        multiplicar = n1 * n2
        print(f"\033[7:34mO resultado de {n1} x {n2} é {multiplicar}\033[m")
    elif opcao == 3:
        if n1 > n2:
            maior_num = n1
        else:
            maior_num = n2

        print(f"\033[7:34mEntre {n1} e {n2} o maior valor é {maior_num}\033[m")
    elif opcao == 4:
        print("Informe os números novamente:")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))

    elif opcao == 5:
        print("\033[1:34mFinalizando...\033[m")
        sleep(2)
    else:
        print("\033[1:31mOpção Inválida. Tente novamente\033[m")

print("\033[1:35mFim do programa! Volte Sempre!\033[m")