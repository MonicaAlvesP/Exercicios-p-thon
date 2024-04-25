"""
    40) Crie um programa que leia duas notas de um aluno e calcule sua média,
    mostrando uma mensagem no final de acordo com a média atingida:

    - Média abaixo de 5.0:
      REPROVADO

    - Média entre 5.0 e 6.9:
      RECUPERAÇÂO

    - Média 7.0 ou superior:
      APROVADO
"""
# Calculo das notas
nota1 = float(input('Primeira nota do Aluno: '))
nota2 = float(input('Segunda nota do Aluno: '))
calc = (nota1 + nota2) / 2

# Analisando as notas
if calc >= 7:
    print('\033[1:30:42mAprovado!\033[m')
elif calc >= 5.0:
    print('\033[1:30:43mRecuperação!\033[m')
else:
    print('\033[1:30:41mReprovado!\033[m')
