nome_completo = input("Digite seu nome e sobrenome: ")
nome, sobrenome = nome_completo.split()
nome_maiusculo = nome.upper()
sobrenome_minusculo = sobrenome.lower()
nome_completo_formatado = nome_maiusculo + sobrenome_minusculo
print(nome_completo_formatado)