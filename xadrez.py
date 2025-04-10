
# xadrez.py
# Jogo de xadrez completo em terminal (versão básica)

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
    destino_peca = tabuleiro[lin_d][col_d]

    if jogador == 1 and not peca.isupper():
        return False, "Movimento inválido: peça não pertence a você."
    if jogador == 2 and not peca.islower():
        return False, "Movimento inválido: peça não pertence a você."

    # Impede capturar peças do mesmo time
    if destino_peca != ".":
        if (peca.isupper() and destino_peca.isupper()) or (peca.islower() and destino_peca.islower()):
            return False, "Não pode capturar uma peça do seu próprio time."

    delta_l = lin_d - lin_o
    delta_c = col_d - col_o

    def caminho_livre():
        if delta_l == 0:  # movimento horizontal
            passo = 1 if delta_c > 0 else -1
            for c in range(col_o + passo, col_d, passo):
                if tabuleiro[lin_o][c] != ".":
                    return False
        elif delta_c == 0:  # movimento vertical
            passo = 1 if delta_l > 0 else -1
            for l in range(lin_o + passo, lin_d, passo):
                if tabuleiro[l][col_o] != ".":
                    return False
        elif abs(delta_l) == abs(delta_c):  # movimento diagonal
            passo_l = 1 if delta_l > 0 else -1
            passo_c = 1 if delta_c > 0 else -1
            for i in range(1, abs(delta_l)):
                if tabuleiro[lin_o + i * passo_l][col_o + i * passo_c] != ".":
                    return False
        return True

    p = peca.lower()

    if p == "p":  # peão
        direcao = -1 if peca.isupper() else 1
        if col_o == col_d:
            if (lin_d - lin_o) == direcao and destino_peca == ".":
                pass
            elif (lin_d - lin_o) == 2 * direcao and lin_o in (6, 1) and tabuleiro[lin_o + direcao][col_o] == "." and destino_peca == ".":
                pass
            else:
                return False, "Movimento inválido para peão."
        elif abs(col_d - col_o) == 1 and (lin_d - lin_o) == direcao and destino_peca != ".":
            pass  # captura diagonal
        else:
            return False, "Movimento inválido para peão."
    elif p == "t":  # torre
        if delta_l != 0 and delta_c != 0:
            return False, "Torre só pode andar em linha reta."
        if not caminho_livre():
            return False, "Há peças no caminho da torre."
    elif p == "c":  # cavalo
        if not ((abs(delta_l) == 2 and abs(delta_c) == 1) or (abs(delta_l) == 1 and abs(delta_c) == 2)):
            return False, "Movimento inválido para cavalo."
    elif p == "b":  # bispo
        if abs(delta_l) != abs(delta_c):
            return False, "Bispo só pode andar na diagonal."
        if not caminho_livre():
            return False, "Há peças no caminho do bispo."
    elif p == "q":  # rainha
        if (delta_l == 0 or delta_c == 0 or abs(delta_l) == abs(delta_c)):
            if not caminho_livre():
                return False, "Há peças no caminho da rainha."
        else:
            return False, "Movimento inválido para rainha."
    elif p == "k":  # rei
        if abs(delta_l) > 1 or abs(delta_c) > 1:
            return False, "O rei só pode se mover uma casa em qualquer direção."
    else:
        return False, "Peça não reconhecida."

    # Movimento válido
    tabuleiro[lin_d][col_d] = peca
    tabuleiro[lin_o][col_o] = "."
    return True, "Movimento realizado com sucesso."

def main():
    tabuleiro = criar_tabuleiro()
    jogador = 1

    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Vez do Jogador {jogador} ({'brancas' if jogador == 1 else 'pretas'})")
        movimento = input("Digite o movimento (ex: e2 e4, ou 'sair' para encerrar): ").strip().lower()

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
            print("Entrada inválida. Use o formato: e2 e4")

if __name__ == "__main__":
    main()
