"""
    62) Melhore o DESAFIO 061, perguntando para o usuário se ele
    quer mostrar mais alguns termos. O programa encerra quando ele
    disser que quer mostrar 0 termos.
"""
print("\033[36mGerador de PA\033[m")
print('-=' * 14)

primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("\033[36mQuantos termos a mais você quer mostrar? \033[m"))
print('FIM')
