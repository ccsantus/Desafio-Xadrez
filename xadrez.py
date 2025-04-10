
# xadrez.py
# Jogo de xadrez simples em terminal - versão inicial

def criar_tabuleiro():
    return [
        ["T", "C", "B", "Q", "K", "B", "C", "T"],
        ["P"] * 8,
        ["."] * 8,
        ["."] * 8,
        ["."] * 8,
        ["."] * 8,
        ["p"] * 8,
        ["t", "c", "b", "q", "k", "b", "c", "t"]
    ]

def imprimir_tabuleiro(tabuleiro):
    print("\n  a b c d e f g h")
    for i, linha in enumerate(tabuleiro):
        print(f"{8 - i} " + " ".join(linha))
    print()

def pos_para_indices(pos):
    colunas = "abcdefgh"
    col = colunas.index(pos[0])
    lin = 8 - int(pos[1])
    return lin, col

def mover(tabuleiro, origem, destino, jogador):
    lin_o, col_o = pos_para_indices(origem)
    lin_d, col_d = pos_para_indices(destino)
    peca = tabuleiro[lin_o][col_o]

    # Verifica se tem peça e se é do jogador certo
    if jogador == 1 and peca.isupper() == False:
        return False, "Movimento inválido: peça não pertence a você."
    if jogador == 2 and peca.islower() == False:
        return False, "Movimento inválido: peça não pertence a você."

    # Movimento de peão (versão simplificada)
    if peca.lower() == "p":
        direcao = -1 if peca.isupper() else 1  # brancas sobem, pretas descem
        if col_o == col_d and tabuleiro[lin_d][col_d] == ".":
            if lin_d - lin_o == direcao:
                tabuleiro[lin_d][col_d] = peca
                tabuleiro[lin_o][col_o] = "."
                return True, "Movimento realizado com sucesso."
            else:
                return False, "Peões só andam 1 casa pra frente por enquanto."

    return False, "Movimento ainda não implementado para essa peça."

def main():
    tabuleiro = criar_tabuleiro()
    jogador = 1

    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Vez do Jogador {jogador} ({'brancas' if jogador == 1 else 'pretas'})")
        movimento = input("Digite o movimento (ex: e2 e4): ").strip().lower()

        if movimento == "sair":
            print("Jogo encerrado.")
            break

        try:
            origem, destino = movimento.split()
            valido, msg = mover(tabuleiro, origem, destino, jogador)
            print(msg)
            if valido:
                jogador = 2 if jogador == 1 else 1
        except Exception as e:
            print("Entrada inválida. Formato correto: e2 e4")

if __name__ == "__main__":
    main()
