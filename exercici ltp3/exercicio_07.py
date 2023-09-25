def analisar_string(string):
    # Inicialize contadores para letras maiúsculas, minúsculas, dígitos e caracteres especiais
    maiusculas = 0
    minusculas = 0
    digitos = 0
    especiais = 0

    # Use o método isalnum() para contar letras maiúsculas, minúsculas e dígitos
    for char in string:
        if char.isupper():
            maiusculas += 1
        elif char.islower():
            minusculas += 1
        elif char.isdigit():
            digitos += 1
        else:
            especiais += 1

    # Divida a string em palavras e conte quantas palavras existem
    palavras = string.split()
    num_palavras = len(palavras)

    # Retorne os resultados
    return maiusculas, minusculas, digitos, especiais, num_palavras

# Solicite a entrada do usuário
entrada = input("Digite uma string: ")

# Chame a função e obtenha os resultados
maiusculas, minusculas, digitos, especiais, num_palavras = analisar_string(entrada)

# Exiba os resultados
print("Letras maiúsculas:", maiusculas)
print("Letras minúsculas:", minusculas)
print("Dígitos:", digitos)
print("Caracteres especiais:", especiais)
print("Número de palavras:", num_palavras)