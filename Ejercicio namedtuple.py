'''

1.- Importe namedtuple y utilizando la misma, cree una clase Pizza con los atributos tamanyo, precio e ingredientes. Luego, cree una lista vacía pizzas.

2.- Dada la lista “pedidos”, agruéguela al código, recorra la misma, cree instancias de la clase Pizza y agregue las mismas a la lista “pizzas”.

3.- Utilizando collections.Counter, cree un objeto ranking_ingredientes que contenga todos los ingredientes de las instancias en la lista “pizzas” (incluyendo repetidos). Luego imprima el ingrediente más utilizado con la cantidad de pedidos que incluyeron el mismo.
** La impresión debe devolver [(‘Queso’, 6)]

4.- Utilizando collections.defaultdict, cree un objeto con el tipo int por defecto. Luego, actualice el objeto con los valores de la variable ranking_ingredientes del paso anterior. Para finalizar, imprima el valor de las claves “Pepperoni” y “Pepinillos”; deben devolver 3 y 0 respectivamente.

5.- Obtenga e imprima en pantalla el precio mínimo y máximo de cada tamaño de pizza existente en la lista “pizzas”. Considere utilizar defaultdict.

'''

pedidos = [
    ["XL", 100, ["Queso", "Jamón"]],
    ["XL", 120, ["Queso", "Pepperoni"]],
    ["M", 80, ["Queso", "Piña"]],
    ["S", 60, ["Queso"]],
    ["M", 70, ["Pepperoni"]],
    ["L", 90, ["Queso", "Pepperoni"]],
    ["L", 80, ["Queso", "Tomates"]],
]

import collections

'''

class Pizzas:

    def __init__(self):
        self.tamanyo = 'S'
        self.precio = 0
        self.ingredientes =["",""]

    @property
    def tamanyo(self):
        return self.tamanyo
    @tamanyo.setter
    def tamanyo(self, tamanyo):
        self.tamanyo = tamanyo
    @property
    def precio(self):
        return self.precio
    @precio.setter
    def precio(self, precio):
        self.precio = precio
    @property
    def ingredientes(self)
        return self.ingredientes
    @ingredientes.setter
    def ingredientes(self,ingredientes):
        self.ingredientes = ingredientes

'''

Pizza = collections.namedtuple("Pizza", "Tamanyo, Precio, ingredientes")

pizzolas = Pizza("S",100, ["Queso", "Pepperoni"])

pizzas = []

for i in pedidos:
    pizzas.append(i)


print(pizzas)
print("")


c_ingredientes = collections.Counter(pizzas)

c_ing = []

for k,v in Pizza:
    c_ing.append(k['ingredientes'])

