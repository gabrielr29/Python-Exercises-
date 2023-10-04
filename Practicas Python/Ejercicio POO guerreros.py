class Guerrero:
    def __init__(self):
        self._vida = 100
        self._estadoArma = 100
        self._estado = "Ataque"
        self._estadoEscudo = 100
    
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, vida):
        self._vida = vida

    @property 
    def estadoArma(self):
        return self._estadoArma
    
    @estadoArma.setter
    def estadoArma(self,estadoArma):
        self._estadoArma = estadoArma    

    @property 
    def estadoEscudo(self):
        return self._estadoEscudo

    @estadoEscudo.setter
    def estadoEscudo(self,estadoEscudo):
        self._estadoEscudo = estadoEscudo    

    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, estado):
        if self._estadoEscudo == 0 and estado == "Defensa":
            raise ValueError("El escudo esta roto!")
        elif not estado == "Ataque" and not estado == "Defensa":
            raise ValueError("Valor de estado invalido!")
        else:
            self._estado = estado

    @property
    def isalive(self):
        if self._vida > 0:
            print("El guerrero sigue en pie")
        else:
            print("El guerrero estiro la pata! Se acabaron sus aventuras")   
       
    def atacar(self, guerrero2):
   
        if(self._vida == 0):
            print("El guerrero esta muerto, por tanto no puede atacar")

        elif(self._estado == "Defensa"):
            print("El guerrero esta en modo defensa, no puede atacar!")    

        elif(self._estadoArma == 0):
            print("El arma esta rota!")

        elif(guerrero2.vida <= 0):
            print("Vas a atacar a un cadaver!")

        elif(guerrero2.estado == "Defensa"):
            
            guerrero2.estadoEscudo = guerrero2.estadoEscudo - 5 
            self._estadoArma = self._estadoArma - 2
            print("Ataque al escudo! Ahora tiene un total de ", guerrero2.estadoEscudo, "puntos de defensa")

        elif(guerrero2.estado == "Ataque"):
         guerrero2.vida = guerrero2.vida - 20
         self._estadoArma = self._estadoArma - 2
         print("Ataque directo, eso tuvo que doler! Ahora solo le quedan ", guerrero2.vida, " puntos de vida")
        
        else:
            pass

    
Pancracio = Guerrero()
Rocky = Guerrero()

Pancracio.atacar(Rocky)
Pancracio.atacar(Rocky)
Rocky.estado = "Defensa"
Pancracio.atacar(Rocky)
Rocky.estado = "Ataque"
print("Rocky tiene ", Rocky.vida, " puntos de vida")
Rocky.atacar(Pancracio)
Rocky.atacar(Pancracio)
Rocky.atacar(Pancracio)
Rocky.atacar(Pancracio)
Rocky.atacar(Pancracio)
print("Pancracio tiene ", Pancracio.vida, " puntos de vida")
Pancracio.isalive
Rocky.atacar(Pancracio)

