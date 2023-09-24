def contagem_de_a(texto):
    contagem = 0
    for letra in texto: 
        if letra.lower() == "a":
            contagem += 1
    return contagem

print(texto_exemplo)
print(f"O texto contém a letra 'a' {contagem_de_a(texto_exemplo)} vezes.")