# Solicita ao usuário que insira uma frase
frase = input("Digite uma frase: ")

# Divide a frase em palavras usando espaços em branco como separadores
palavras = frase.split()

# Conta o número de palavras na frase
numero_de_palavras = len(palavras)

# Concatena as palavras em uma única string sem espaços em branco
frase_sem_espacos = ''.join(palavras)

# Converte a frase para letras maiúsculas
frase_maiuscula = frase_sem_espacos.upper()

# Imprime o número de palavras e a frase em letras maiúsculas sem espaços em branco
print(f"Número de palavras na frase: {numero_de_palavras}")
print(f"Frase em letras maiúsculas sem espaços: {frase_maiuscula}")