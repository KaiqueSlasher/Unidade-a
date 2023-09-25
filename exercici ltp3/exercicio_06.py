def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    escolha = input("Escolha uma opção:\n1. Celsius para Fahrenheit\n2. Fahrenheit para Celsius\n")
    
    if escolha == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        casas_decimais = int(input("Digite o número de casas decimais desejado: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"A temperatura em Fahrenheit é: {round(fahrenheit, casas_decimais)}")
    elif escolha == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        casas_decimais = int(input("Digite o número de casas decimais desejado: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"A temperatura em Celsius é: {round(celsius, casas_decimais)}")
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()