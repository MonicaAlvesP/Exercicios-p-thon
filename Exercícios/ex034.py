"""

      Escreva um programa que pergunte o salário de um funcionário e calcule
    o valor do seu aumento.
      Para salários superiores a R$ 1.306.00, calcule um aumento de 10%.
      Para salários inferiores ou iguais , e aumente é de 15%.

"""

salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1306:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print(f'Quem ganhava \033[1:34mR${salario}\033[m passa a ganhar \033[1:34mR${novo}\033[m agora.')
