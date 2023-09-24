def palindromo():
    nome = input("Digite um nome: ")
    if nome == nome[::-1]:
        print("É palíndromo")
    else:
        print("Não é palíndromo")

palindromo()