"""
    41) A Confederação Nacional de Natação precisa de um programa que leia
    o ano de nascimento de um atleta e mostre sua categoria, de acordo com
    a idade:

    - Até 9 anos: MIRIM
    - Até 14 anos: INFANTIL
    - Até 19 anos: JÚNIOR
    - Até 20 anos: SÊNIOR
    - Acima: MASTER
"""
from datetime import date

# Coletando dados
ano_nascimento = int(input('Informe o ano do seu nascimento: '))

# Calculando o ano de nascido
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

# Definindo as Categorias

if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JÙNIOR'
elif idade <= 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

# Resultado
print(f"\033[36mA categoria do Atleta é \033[m: \033[1:30:46m{categoria}\033[m")
