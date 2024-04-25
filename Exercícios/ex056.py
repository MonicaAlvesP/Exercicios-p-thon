"""
    56) Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas.
    No final do programa, mostre:
    · A média de idade do grupo
    · Qual é o nome do homem mais velho
    · Quantas mulheres têm menos de 20 anos.
"""
soma_idade = 0
media_de_idade = 0
maior_idade_H = 0
nome_do_maisVelho = ''
total_de_M20 = 0

for p in range(1, 5):
    print("_____ {}ª PESSOA _____".format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade

    if p == 1 and sexo in 'Mm':
        maior_idade_H = idade
        nome_do_maisVelho = nome

    if sexo in 'Mm' and idade > maior_idade_H:
        maior_idade_H = idade
        nome_do_maisVelho = nome

    if sexo in 'Ff' and idade < 20:
        total_de_M20 += 1

media_de_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos'.format(media_de_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_H, nome_do_maisVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(total_de_M20))
