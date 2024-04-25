"""

    Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
    o primeiro e o qúltimo nome separadamente.

    EX: Ana Maria de Souza
        primeiro = Ana
        ultimo = Souza

"""

n = str(input("Digite seu nome Completo: ")).strip()
nome = n.split()
print('Prazer em te conhecer!')
print(f"Seu primeiro nome é \033[1:30:45m{nome[0]}\033[m")
print(f"Seu último nome é \033[1:30:45m{nome[-1]}\033[m")
