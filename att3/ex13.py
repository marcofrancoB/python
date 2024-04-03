
sandwich_orders = ["sanduíche de atum", "sanduíche de frango", "sanduíche de queijo"]
finished_sandwiches = []
while sandwich_orders:
    pedido = sandwich_orders.pop(0)  
    print("Preparando seu", pedido + ".")
    finished_sandwiches.append(pedido)
print("\nSanduíches preparados:")
for sanduiche in finished_sandwiches:
    print("- " + sanduiche)
