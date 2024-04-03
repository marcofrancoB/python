versao_inicial = [1, 2, 3, 4, 5]

versao_alterada = [2, 3, 5, 6, 7]

conjunto_versao_inicial = set(versao_inicial)
conjunto_versao_alterada = set(versao_alterada)

elementos_nao_mudaram = conjunto_versao_inicial.intersection(conjunto_versao_alterada)

novos_elementos = conjunto_versao_alterada.difference(conjunto_versao_inicial)

elementos_removidos = conjunto_versao_inicial.difference(conjunto_versao_alterada)

print("Elementos que não mudaram:", elementos_nao_mudaram)
print("Novos elementos:", novos_elementos)
print("Elementos removidos:", elementos_removidos)
