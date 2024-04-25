"""

    Escreva um programa que converta uma temperatura digitada em °C e converta para °F

"""

celsius = float(input("Informe a temperatura em °C: "))
fahrenheit = 9 * celsius / 5 + 32

print(f"A temperatura de \033[34m{celsius}\033[m°C corresponde a \033[34m{fahrenheit}\033[m°F!")
