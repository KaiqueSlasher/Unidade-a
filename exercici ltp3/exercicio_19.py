from datetime import datetime

def calcular_idade(data_nascimento, data_atual):
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    data_atual = datetime.strptime(data_atual, "%d/%m/%Y")
    idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))
    return idade

# Solicita que o usuário insira a data de nascimento
data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")

# Solicita que o usuário insira a data atual
data_atual = input("Digite a data atual (DD/MM/AAAA): ")

# Calcula a idade
idade = calcular_idade(data_nascimento, data_atual)

# Exibe a idade calculada
print(f"Sua idade é {idade} anos.")