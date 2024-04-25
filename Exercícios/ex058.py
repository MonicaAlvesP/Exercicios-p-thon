"""
    58) Melhore o jogo do DESAFIO 028 onde o computador vai
    'pensar' em um número entre 0 e 10. Só que agora o jogador vai
    tentar adivinhar até aertar, mostrando no final quantos palpites
    foram nescessários para vencer.
"""
from random import randint

computador = randint(0, 10)
acertou = False
palpites = 0

print("Sou seu computador...")
print("Acabei de pensar em um número entre \033[34m0\033[m e \033[34m10\033[m")
print("Será que você consegue adivinhar qual foi?")
while not acertou:
    jogador = int(input("Qual é o seu palpite?  "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez.")
        elif jogador > computador:
            print("Menos... Tente mais uma vez.")

print(f"\033[34mParabéns, você acertou com {palpites} tentativas!\033[m")
