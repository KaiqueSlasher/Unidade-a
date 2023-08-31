def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

def contar_vogais(texto):
    vogais = "aeiou"
    texto = texto.lower()
    contador = 0
    for char in texto:
        if char in vogais:
            contador += 1
    return contador

def substituir_python_por_java(texto):
    return texto.replace("Python", "Java")

def converter_para_minusculas(texto):
    return texto.lower()

def palavras_unicas(texto):
    palavras = texto.lower().split()
    palavras_unicas = list(set(palavras))
    return palavras_unicas

def imprimir_ordem_alfabetica(texto):
    palavras = texto.lower().split()
    palavras.sort()
    return palavras

def main():
    while True:
        print("\nMenu:")
        print("1. Conte o número total de palavras digitadas.")
        print("2. Conte o número de vogais na palavra digitada.")
        print("3. Substitua todas as ocorrências da palavra 'Python' por 'Java'.")
        print("4. Converta todas as letras da string para minúsculas.")
        print("5. Crie uma lista com todas as palavras únicas encontradas na string.")
        print("6. Imprima as palavras na string em ordem alfabética.")
        print("7. Sair")
        
        escolha = input("Digite a opção desejada: ")
        
        if escolha == '1':
            texto = input("Digite o texto: ")
            print("Número total de palavras:", contar_palavras(texto))
        elif escolha == '2':
            texto = input("Digite o texto: ")
            print("Número de vogais:", contar_vogais(texto))
        elif escolha == '3':
            texto = input("Digite o texto: ")
            print(substituir_python_por_java(texto))
        elif escolha == '4':
            texto = input("Digite o texto: ")
            print(converter_para_minusculas(texto))
        elif escolha == '5':
            texto = input("Digite o texto: ")
            print("Palavras únicas:", palavras_unicas(texto))
        elif escolha == '6':
            texto = input("Digite o texto: ")
            print("Palavras em ordem alfabética:", imprimir_ordem_alfabetica(texto))
        elif escolha == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Digite uma opção válida.")

if __name__ == "__main__":
    main()