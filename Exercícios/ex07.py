"""

Desenvolva um programa que leia as notas de um aluno, calcule e mostre a sua média.

"""

nota1 = float(input('Primeira nota do Aluno: '))
nota2 = float(input('Segunda nota do Aluno: '))
calc = (nota1 + nota2) / 2

if calc >= 7:
    print('Aprovado!')
elif calc >= 5:
    print('Recuperação!')
else:
    print('Reprovado!')

print(f"A média entre \033[1:36m{nota1}\033[m e \033[1:36m{nota2}\033[m é igual a \033[1:36m{calc}\033[m!")
