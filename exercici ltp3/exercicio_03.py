import random
import string

def gerar_senha(comprimento, qtd_letras, qtd_numeros, qtd_especiais):
    letras = string.ascii_letters
    numeros = string.digits
    especiais = string.punctuation

    caracteres = []

    for _ in range(qtd_letras):
        caracteres.append(random.choice(letras))

    for _ in range(qtd_numeros):
        caracteres.append(random.choice(numeros))

    for _ in range(qtd_especiais):
        caracteres.append(random.choice(especiais))

    while len(caracteres) < comprimento:
        caracteres.append(random.choice(letras + numeros + especiais))

    random.shuffle(caracteres)

    senha = ''.join(caracteres)

    return senha

comprimento = int(input("Comprimento da senha: "))
qtd_letras = int(input("Quantidade de letras na senha: "))
qtd_numeros = int(input("Quantidade de números na senha: "))
qtd_especiais = int(input("Quantidade de caracteres especiais na senha: "))

senha_gerada = gerar_senha(comprimento, qtd_letras, qtd_numeros, qtd_especiais)
print("Senha gerada:", senha_gerada)