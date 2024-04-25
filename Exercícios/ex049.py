"""
    49) Refaça o DESAFIO 9, mostrando a tabuada de um número que
    o úsuario escolher, só que agora utilizando um LAÇO FOR.
"""
num = int(input("Digite um número para ver sua tabuada: "))
for c in range(1, 11):
    print("{} = {:2} = {}".format(num, c, num*c))
