pet1 = {
    "nome": "Bolinha",
    "tipo": "Cachorro",
    "dono": "Ana"
}

pet2 = {
    "nome": "Miau",
    "tipo": "Gato",
    "dono": "Pedro"
}

pet3 = {
    "nome": "Pipoca",
    "tipo": "Coelho",
    "dono": "Carla"
}
pets = [pet1, pet2, pet3]

for pet in pets:
    print("Nome:", pet["nome"])
    print("Tipo:", pet["tipo"])
    print("Dono:", pet["dono"])
    print()  