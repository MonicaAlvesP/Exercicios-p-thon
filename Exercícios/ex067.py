"""
    67) Faça um programa que mostre a tabuada de vários números,
    um de cada vez, para cada valor digitado pelo usuário. O pro-
    grama será interrompido quando o número solicitado for nega-
    tivo.
"""
while True:
    valor = int(input("Digite o número do qual deseja ver a tabuada? "))
    if valor < 0:
        break
    else:
        for i in range(1, 11):
            print(f"{valor} x {i:2} = {valor * i:2}")
print('-' * 45)
print("PROGRAMA DE TABUADA ENCERRADO! volte sempre..")
