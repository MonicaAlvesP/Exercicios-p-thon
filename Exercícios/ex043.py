"""
    43) Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
    calcule seu IMC e mostre seu status de acordo com a tabela abaixo:

    - Abaixo de 18.5: Abaixo de Peso.
    - Entre 18.5 e 25: Peso ideal.
    - 25 até 30: Sobrepeso.
    - 30 até 40: Obesidade.
    - Acima de 40: Obesidade morbida.
"""
# Coletando dados
peso = float(input('Informe seu peso: (kg) '))
altura = float(input('Informe sua altura: (m) '))

# calculando o iMC
imc = peso / (altura ** 2)
print(f'\033[1:36mSeu IMC é de {imc:.1f}\033[m')

# Definindo status
if imc < 18.5:
    print('\033[7:35mVocê está ABAIXO do PESO NORMAL!\033[m')
elif 18.5 <= imc < 25:
    print('\033[7:34mVocê está na faixa de PESO NORMAL!\033[m')
elif 25 <= imc < 30:
    print('\033[7:31mVocê está com SOBREPESO!\033[m')
elif 30 <= imc < 40:
    print('\033[7:31mVocê está com OBESIDADE!\033[m')
else:
    print('\033[7:31mVOCÊ ESTÁ COM OBESIDADE MORBIDA, CUIDADO!\033[m')
