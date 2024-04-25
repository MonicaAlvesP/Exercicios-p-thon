"""

    Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

"""

salario_atual = float(input('Qual é o salário do funcionário? R$'))
valor_do_aumento = salario_atual * 15 / 100
salario_final = salario_atual + valor_do_aumento
print(f'O funcionário que ganhava R$\033[1:32m{salario_atual:.2f}\033[m, após o aumento de 15%, ele passa a receber '
      f'R$\033[1:32m{salario_final:.2f}\033[m')
