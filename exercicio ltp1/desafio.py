def create_ascii_art(character, height):
    for i in range(1, height + 1):
        print(character * i)

def main():
    user_character = input("Insira um caractere para o padrão de arte: ")
    user_height = int(input("Insira a altura do padrão de arte (número inteiro positivo): "))

    if user_height <= 0:
        print("A altura deve ser um número inteiro positivo.")
    else:
        create_ascii_art(user_character, user_height)

if __name__ == "__main__":
    main()