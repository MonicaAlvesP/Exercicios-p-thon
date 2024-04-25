"""

 Estrutura condicional aninhada!

"""
nome = str(input("Qual é o seu nome: "))
if nome == 'Mônica':
    print("Que nome bonito!")
elif nome == 'Bernardo' or nome == 'Caio' or nome == 'Júnior':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é bem normal!')
print(f"\033[1:36mTenha um bom dia, {nome}!")
