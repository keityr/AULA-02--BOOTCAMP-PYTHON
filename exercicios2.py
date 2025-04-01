# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar 
# ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, 
# tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for
#  válida.

# try:
#     celsius = float(input("Temperatura em Celsius: "))
#     fahrenheit = celsius * 1.8 + 32 
#     print("fahrenheit: " , fahrenheit)

# except ValueError as e:
#     print("Erro:", e)
    


# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para
#  frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.


# texto = input("Digite uma palavra ou frase: ").lower().replace(" ", "").replace(",", "").replace(".", "")
# if texto == texto[::-1]:
#     print("É um palíndromo!")
# else:
#     print("Não é um palíndromo.")



# Exercício 23: Calculadora Simples

# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário.
#  Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar
#  a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

# print("Calculadora")
# try:
#     num1 = float(input("Número: "))
#     ope = str(input("Operação: "))
#     num2 = float(input("Número: ")) 

#     if ope == '+':
#         soma = num1 + num2
#         print("Soma:", soma)

#     elif ope == "-":
#         sub = num1 - num2
#         print("Substração:", sub)

#     elif ope == "/":
#         if num2 == 0:
#             print("Não foi possível dividir por zero!")
#         else:
#             div = num1 / num2
#             print("Divisão:", div)

#     elif ope == "*":
#         mult = num1 * num2
#         print("Multiplicação:", mult)

#     else:
#         print("Operação inválida! Use +, -, *, ou /.")

# except ZeroDivisionError:
#     print("Você está tentando dividir por zero!")

# except ValueError:
#     print("Você inseriu algo diferente de Número!")


# Exercício 24: Classificador de Número

# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a 
# entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero".
#  Adicionafiquelmente, identi se o número é "par" ou "ímpar".

# try:
#     num1 = float(input("Digite um número: "))

#     if num1 > 0:
#         print("É positivo!")
              
#     elif num1 < 0:
#         print('É negativo!')
    # else:
    #     print("Zero")
    # if numero % 2 == 0:
    #     print("Par")
    # else:
    #     print("Ímpar")

# except ValueError:
#     print("Você não digitou um número válido!")



# Exercício 25: Conversão de Tipo com Validação

# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter
#  a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada 
# número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento
#  não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos,
#  imprima a lista de inteiros.

try:
    # Solicita a entrada do usuário e divide em uma lista de strings
    numeros = input("Digite uma lista de números separados por vírgula (ex: 1,2,3,4): ").split(",")
    
    # Tenta converter cada elemento da lista para um número inteiro
    inteiros = [int(num.strip()) for num in numeros]  # strip() remove espaços extras

    # Se todas as conversões forem bem-sucedidas, imprime a lista
    print("Lista de inteiros:", inteiros)

except ValueError:
    print("Erro: Algum valor não é um número inteiro válido.")