Pizza = collections.namedtuple("Pizza", "Tamanyo", "Precio", ["Ingrediente1", "Ingrediente2"], rename=True)

pizzolas = Pizza("S",100,["Pepperoni", "Queso"])

print(pizzolas)