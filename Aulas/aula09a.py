"""

    Cadeia de Caracters

"""

frase = 'Curso em Vídeo Python'
''' Fatiamento
    EM FATIAMENTO O ÚLTIMO VALOR SEMPRE SERÁ IGNORADO PELO PYTHON

 print(frase[9:21])  # pegou do índice 9 até o 21
 print(frase[9:21:2])  # Pula de 2 em , do índice 9 ao 21
 print(frase[:5]) # Vai começar do início até 5
 print(frase[15:])  # Pega do caracter 15 até o final, pois não especifica onde deve parar

'''

'''

Análise

print(len(frase))  # Analisa o Tamanho da frase
print(frase.count('o')  # Conta quantas vezes tem a letra 'o' minúscula
print(frase.find('deo)  # Diz quantas vezes encontrou a palavra 'deo', conta desde o primeiro índice
'Curso' in frase  # Diz se existe a palavra 'Curso' no frase

'''

'''

Transformação

frase.replace('Python', 'Android') # Substitui a palavra "Python" por "Android"
frase.upper()  # Tudo ficara em caixa alta = upper é um method
frase.lower()  # Tudo ficara em caixa baixa, minuscula
frase.capitalize()  # Somente a primeira letra da palavra ficará em caixa alta = como num titulo
frase.title()  # Onde conter espaços, a proxima palavra iniciara com caixa alta
frase.strip()  # Remove todos os espaços inuteis

'''

'''

Divisão

frase.split() # Divide uma string em uma lista

'''

'''

Junção

'-'.join(frase)  # Junta uma frase na outra, separando com o trassinho 

'''
