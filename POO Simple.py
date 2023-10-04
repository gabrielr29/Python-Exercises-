class Humano:
    def atacar(self):
        print("puño")
class Guerrero(Humano):
    def atacar(self):
        print("espadazo")
class Mago(Humano):
    def atacar(self):
        print("hechizo")
class Rey(Humano):
    pass
class Brujo(Rey,Mago):
    pass

brujito = Brujo()
print(brujito.atacar())
print(Brujo.__)
