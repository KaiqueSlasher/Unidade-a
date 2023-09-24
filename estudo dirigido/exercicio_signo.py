def signo_chines(ano):
    signo_chines = ["Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Cabra", "Macaco", "Galo", "Cão", "Porco"]
    calculo = (ano - 1900) % 12
    return signo_chines[calculo]

print(signo_chines(int(input("Digite o ano de nascimento: "))))