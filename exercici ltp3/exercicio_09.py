def calcular_imc(peso, altura):
    # Calcula o IMC
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    # Classifica o IMC
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 24.9 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obeso"

# Solicita ao usuário o peso e a altura
peso = float(input("Digite o peso em quilogramas: "))
altura = float(input("Digite a altura em metros: "))

# Calcula o IMC
imc = calcular_imc(peso, altura)

# Classifica o IMC e fornece uma indicação
classificacao = classificar_imc(imc)

# Exibe o IMC e a classificação
print(f"Seu IMC é {imc:.2f}")
print(f"Classificação: {classificacao}")