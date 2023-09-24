def eh_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    else:
        for num in range(2, numero):
            if numero % num == 0:
                return False
        return True
    
numero = int(input("Digite um número inteiro: ")) 
print(eh_primo(numero))