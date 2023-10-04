#Calculo del factorial de un número

def Factorial(n):
    a = 1
    for i in range(1,n+1):
        a = a * i
    return a

def Read_n():
    Wkey = 0

    while(Wkey==0):
        n1 = str(input("Ingrese un numero para calcular el factorial: "))
        try:
          n1 = (int)(n1)
        except ValueError:
          print("Error, no es un numero entero")
        else:
           if(n1<=0):
             print("Error, numero invalido")
           elif(n1>500):
              print("Fuera de rango, max 500")
           else:   
              Wkey=1

    return n1      

n = Read_n()
print("El factorial del numero ingresado es: ", Factorial(n))

