# inicio do projeto + possíveis dados que iremos usar
          #sistema de senhas para clientes que chegam na agência

# 1) Dados de entrada 
atendimento_preferencial = '1'
atendimento_convencional = '2'
tipo_de_atendimento = input('Qual o tipo de atendimento 1 ou 2')

# Serviços realizados 
serviços = {'abertura de contas': 1, 'saque/caixas': 2, 'Empréstimos': 3, 'Financiamentos': 4, 'Empresas': 5}


# 2) Processamento dos dados 
def senha_aleatória(senha):
    letras = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'x', 'c']
    numeros = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]
    while letra in letras and numero in numeros:
        print('Criar senha!!')
        senha = letra[0, 0, 0] + numero[0, 0, 0]
        print(senha) 


# 3) Saida (O que irá ser executado e mostrado)



