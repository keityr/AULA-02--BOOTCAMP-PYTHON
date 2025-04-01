#O programa deve começar solicitando ao usuário que insira seu nome.
CONSTANTE_BONUS =  1000


#nome = str(input("Digite seu nome: "))

while True:

    try:
        nome_usario =str(input("Diga seu nome: "))

        if nome_usario.isdigit():
            print("vc digitou o nome errado! Digite novamente: ")

        elif len(nome_usario) == 0:
            print("Você não digitou nada!")

        elif nome_usario.isspace():
            print("Você digitou apenas espaços!")

        else:
            print("Nome cadastrado com sucesso!")
            break
    except ValueError:
        print("Nome inválido!")
    

#Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser 
# um número decimal.
while True:

    try:
        salario = float(input("Qual seu salário?: "))

        if salario < 0:
            print("O salário não pode ser negativo! Tente novamente: ")
            continue

        elif salario == 0:
            print("Seu salário não pode ser zero. Digite um salário válido: ")
            continue

            
        print("Salário Válido")
        break
            
    except ValueError:
        print("Você inseriu um número inválido ")



#Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.

while True:
    try:
        bonus = float(input("Informe a  porcentagem de bônus recebido: "))

        if bonus < 0:
            print("O bonus não pode ser negativo!")
            continue
        break
    except ValueError:
        print("O valor inserido não é um numero, faça novamente: ")

# cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus

kpi = CONSTANTE_BONUS + salario * bonus

#Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 500"

print(f"Olá {nome_usario}, o seu valor bônus foi de R$ {kpi:.2f}") 