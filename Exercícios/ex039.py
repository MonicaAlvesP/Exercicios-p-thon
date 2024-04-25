"""
    39) Faça um programa que leia o ano de nascimento de um jovem e informe,
    de acordo com dua idade:

    - Se ele ainda vai se alistar ao serviço militar.
    - Se é a hora de se alistar.
    - Se já passou do tempo do alistamento.

    Seu programa também deve mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date

# Ano de nascimento
ano_nascimento = int(input('Informe o ano do seu nascimento: '))

# Calculando
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(f'\033[37mQuem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}\033[m')
alistamento = 18

if idade < alistamento:
    tempo_restante = alistamento - idade
    faltam = ano_atual + tempo_restante
    print(f"\033[1:34mAinda faltam {tempo_restante} anos para o seu alistamento!\033[m")
    print(f'\033[1:34mSeu alistamento será em {faltam}\033[m')
elif idade == alistamento:
    print(f"\033[7:34mEstá na hora de você se alistar!\033[m")
else:
    tempo_passado = idade - alistamento
    passou = ano_atual - tempo_passado
    print(f'\033[1:31mJá passou {tempo_passado} anos do tempo de alistamento!\033[m')
    print(f'\033[1:31mSeu alistamento foi em {passou}')
