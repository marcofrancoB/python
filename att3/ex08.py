# Duas listas de exemplo
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

valores_comuns = conjunto1.intersection(conjunto2)

valores_apenas_na_primeira = conjunto1.difference(conjunto2)

valores_apenas_na_segunda = conjunto2.difference(conjunto1)

elementos_nao_repetidos = list(conjunto1.union(conjunto2))

primeira_sem_repetidos_na_segunda = list(conjunto1.difference(conjunto2))

print("Valores comuns às duas listas:", valores_comuns)
print("Valores que só existem na primeira lista:", valores_apenas_na_primeira)
print("Valores que existem apenas na segunda lista:", valores_apenas_na_segunda)
print("Lista com elementos não repetidos das duas listas:", elementos_nao_repetidos)
print("A primeira lista sem os elementos repetidos na segunda:", primeira_sem_repetidos_na_segunda)
