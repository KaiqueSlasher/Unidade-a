nome_completo = input("Digite seu nome e sobrenome: ")
nome_usuário, sobrenome_usuario = nome_completo.split()
nome_completo = nome_usuário.upper() + " " + sobrenome_usuario.upper()
print("Nome completo em letras minúsculas:", nome_completo.lower())
tamanho_nome_completo = len(nome_completo)
print("Tamanho do nome completo:", tamanho_nome_completo)