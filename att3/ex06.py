lugares_vagos = [10, 2, 1, 3, 0]

while True:
    sala = int(input("Digite o número da sala (ou 0 para sair): "))
    if sala == 0:
        print("Encerrando o programa...")
        break
    elif sala < 1 or sala > len(lugares_vagos):
        print("Sala inválida. Digite um número de sala válido.")
        continue

    lugares_solicitados = int(input("Digite a quantidade de lugares solicitados: "))

    if lugares_solicitados > lugares_vagos[sala - 1]:
        print("Desculpe, não há lugares suficientes disponíveis nessa sala.")
    else:
        lugares_vagos[sala - 1] -= lugares_solicitados
        print(f"Bilhetes vendidos com sucesso para a sala {sala}.")
        print(f"Lugares restantes na sala {sala}: {lugares_vagos[sala - 1]}")

print("Obrigado por utilizar nosso sistema!")
