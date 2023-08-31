def remove_vowels(text):
    vowels = "AEIOUaeiou"
    text_without_vowels = ''.join([char for char in text if char not in vowels])
    return text_without_vowels

def main():
    user_input = input("Digite um texto: ")
    result = remove_vowels(user_input)
    print("Texto sem vogais:", result)

if __name__ == "__main__":
    main()