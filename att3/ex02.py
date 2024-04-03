import random
palavras = ['casa', 'sala', 'goiaba', 'algoritmo', 'software']

def escolher_palavra(palavras):
  
    indice = random.randint(0, len(palavras) - 1)
    return palavras[indice]

def mostrar_palavra(palavra, letras_corretas):
    palavra_mostrada = ''
    for letra in palavra:
        if letra in letras_corretas:
            palavra_mostrada += letra + ' '
        else:
            palavra_mostrada += '_ '
    return palavra_mostrada.strip()

def jogar_forca():
    palavra = escolher_palavra(palavras)
    letras_corretas = []
    tentativas = 6  # Número de tentativas
    letras_erradas = []

    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra tem", len(palavra), "letras.")

    while tentativas > 0:
        print("\nPalavra:", mostrar_palavra(palavra, letras_corretas))
        print("Letras erradas:", letras_erradas)
        print("Tentativas restantes:", tentativas)
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou esta letra. Tente novamente.")
            continue

        if letra in palavra:
            print("Ótimo! A letra", letra, "está na palavra.")
            letras_corretas.append(letra)
        else:
            print("Ops! A letra", letra, "não está na palavra.")
            letras_erradas.append(letra)
            tentativas -= 1

        # Verificar se o jogador acertou todas as letras
        if all(letra in letras_corretas for letra in palavra):
            print("\nParabéns! Você acertou a palavra:", palavra)
            break

    if tentativas == 0:
        print("\nVocê perdeu! A palavra correta era:", palavra)


jogar_forca()
