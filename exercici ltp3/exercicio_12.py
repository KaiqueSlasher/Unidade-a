def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas, colunas e diagonais
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or \
           all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or \
       all([tabuleiro[i][2 - i] == jogador for i in range(3)]):
        return True
    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    vitorias = {"X": 0, "O": 0}

    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Vitórias - X: {vitorias['X']}, O: {vitorias['O']}")

        linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1, 2): "))
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1, 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
        else:
            print("Essa posição já está ocupada. Tente novamente.")
            continue

        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            vitorias[jogador_atual] += 1
            break

        if " " not in [posicao for linha in tabuleiro for posicao in linha]:
            imprimir_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    jogar_jogo_da_velha()
