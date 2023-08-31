def substituir_vogais():
    palavra = input("Digite uma palavra: ")
    palavra = palavra.lower()  # Converte a palavra para minúsculas
    
    vogais = ['a']
    
    nova_palavra = ''
    for letra in palavra:
        if letra in vogais:
            nova_palavra += '*'
        else:
            nova_palavra += letra
    
    print("Palavra substituída:", nova_palavra)

# Executa a função
substituir_vogais()