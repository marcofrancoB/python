def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2-i] == jogador for i in range(3)]):
        return True
    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ['X', 'O']
    jogador_atual = 0

  
    for _ in range(9):  
        print("Jogador", jogadores[jogador_atual], "é sua vez.")

        
        while True:
            linha = int(input("Escolha a linha (0, 1, 2): "))
            coluna = int(input("Escolha a coluna (0, 1, 2): "))
            if tabuleiro[linha][coluna] == " ":
                break
            else:
                print("Essa posição já está ocupada. Escolha outra.")

        tabuleiro[linha][coluna] = jogadores[jogador_atual]

        if verificar_vitoria(tabuleiro, jogadores[jogador_atual]):
            imprimir_tabuleiro(tabuleiro)
            print("Jogador", jogadores[jogador_atual], "venceu!")
            return

     
        jogador_atual = (jogador_atual + 1) % 2

    
    imprimir_tabuleiro(tabuleiro)
    print("Empate!")

jogar_jogo_da_velha()
