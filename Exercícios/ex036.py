"""
    36) Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
ele vai pagar.

 e Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou
 então o empréstimo será negada.

"""
# Recebendo o valor da casa
casa = float(input("Informe o valor da casa: R$"))

# Recebendo o salário do comprador
salario = float(input("Salário do comprador: R$"))

# Recebendo a quantidade de anos para pagar
anos = int(input("Em quantos anos você deseja pagar: "))

# Calculando o valor da prestação mensal
prestacao = casa / (anos * 12)

# Verificando se o valor da prestação é menor que 30% do salário
if prestacao < (salario * 0.3):
    print("\033[1:32mEmpréstimo aprovado!\033[m")
    print(f"Valor da prestação: \033[1:34mR${prestacao:.2f}")
else:
    print("\033[1:31mEmpréstimo negado!")

print(f'\033[30:43mPara pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}!\033[m')
