"""

    Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule
    o preço da passagem, cobrando R$0.50 por km para viagens dde até 200km e R$0.45
    para viagens mais longe.

"""

distancia = float(input("Qual é o preço da sua viagem? "))
print(f"Você esta prestes a começar uma viagem de \033[1:34m{distancia}km\033[m")
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"E o preço da sua passagem será de \033[1:34mR${preco:.2f}")
