print("Bem-vindo ao Jogo de Adivinhação!")
print(f"Você tem um total de {max_tentativas} tentativas para adivinhar o número.")

while tentativas < max_tentativas:
    # Solicitar uma tentativa ao usuário
    try:
        tentativa = int(input("Digite um número: "))
    except ValueError:
        print("Isso não parece ser um número válido. Tente novamente.")
        continue

    tentativas += 1

    # Verificar se a tentativa está correta
    if tentativa == numero_aleatorio:
        print(f"Parabéns! Você adivinhou o número {numero_aleatorio} em {tentativas} tentativas.")
        break
    elif tentativa < numero_aleatorio:
        print("O número é maior. Tente novamente.")
    else:
        print("O número é menor. Tente novamente.")

if tentativas == max_tentativas:
    print(f"Suas {max_tentativas} tentativas acabaram. O número correto era {numero_aleatorio}. O jogo acabou.")