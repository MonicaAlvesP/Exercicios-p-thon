""" nome = str(input('Qual é o seu nome? '))
if nome == 'Mônica':               # ESTE BLOCO SÓ VAI ACONTECER SE TIVER O NOME 'MÔNICA'
    print('Seu nome é perfeito!')
else:
    print('Bah! Teu nome é tão normal..')
print(f'Bom Dia {nome}') """

n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
m = (n1 + n2) / 2
if m >= 7.0:
    print("Parabéns! Você foi Aprovado.")
else:
    print("Sinto Muito! Você foi Reprovado.")

print(f"A sua média foi {m}")
