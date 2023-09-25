import random

# Lista de respostas possíveis
respostas = ["Sim", "Não", "Talvez"]

# Função para gerar uma resposta aleatória
def gerar_resposta():
    return random.choice(respostas)

# Função principal
def main():
    while True:
        pergunta = input("Faça uma pergunta (ou digite 'sair' para encerrar): ")
        
        if pergunta.lower() == "sair":
            break
        
        resposta = gerar_resposta()
        print(f"Resposta: {resposta}\n")

if __name__ == "__main__":
    main()
