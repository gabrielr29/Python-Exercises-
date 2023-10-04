#Cree una clase Punto que reciba las coordenadas (x, y) y un método que indique a qué cuadrante pertenece.

#PARA VALIDAR, CODIGO DE: http://agrportfolioeducativo.blogspot.com/2016/05/31-la-clase-punto.html

import math

def es_numero(num):
    # indica si es o no un valor numérico
    return isinstance (num, (int, float, complex))


class Punto: 

    def __init__(self, coordx, coordy):

        if not(es_numero(coordx)) or not(es_numero(coordy)):
           raise TypeError("Solo se permiten numeros")
        else :
         self._coordx = coordx
         self._coordy = coordy 
 
    @property
    def coordx(self):
        return self._coordx

    @coordx.setter
    def coordx(self, coordx):
        self._coordx = coordx

    @property
    def coordy(self):
        return self._coordy

    @coordy.setter
    def coordy(self, coordy):
        self._coordx = coordy
   
    @property
    def cuadrante(self):
     if self._coordx > 0 and self._coordy > 0:
        return "Cuadrante I"
     elif self._coordx < 0 and self._coordy > 0:
        return  "Cuadrante II"
     elif self._coordx < 0 and self._coordy < 0:
        return "Cuadrante III"
     elif self._coordx > 0 and self._coordx > 0:
        return "Cuadrante IV"
     elif self.coordx == 0:
        return "Eje Y"
     elif self.coordy == 0:
        return "Eye X"
     elif self.coordx == 0 and self.coordy == 0:
        return "Origen"
     
class Vector(Punto):
   def __init__(self,a, b):
      self._a = a
      self._b = b

   @property
   def distancia(self):
      ab = math.sqrt(pow((self._b.coordx-self._a.coordx),2) + pow((self._b.coordy-self._a.coordy),2))
      return ab         

punto = Punto(68,75)
puntillo = Punto(32,-58)

vector = Vector(punto, puntillo)
print("La distancia entre los puntos del vector es: ", vector.distancia)