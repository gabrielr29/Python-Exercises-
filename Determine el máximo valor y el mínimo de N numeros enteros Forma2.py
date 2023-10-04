#Determine el máximo valor y el mínimo valor de N números enteros (Forma 2)

def Max_or_Min(n1, n2):
  if n1 > n2:
    return 1
  elif n1 < n2:
    return 2
  else:
    return 0
  
def Imprimir_inf(n1,n2):
    if Max_or_Min(n1, n2)==1:
      print("El mayor es ", n1, "Y el menor ", n2)
    elif  Max_or_Min(n1, n2)==2:
      print("El mayor es ", n2, "Y el menor ", n1)
    else:
       print("Ambos numeros son iguales")

n1 = 0
n2 = 0
max = 0
min = 0
nrepeats = 0

print("Bienvenido a este comparador de numeros","\n")
nrepeats = int(input("Ingrese la cantidad de numeros que desea comparar: "))

if(nrepeats>2):

  n1 = int(input("Ingrese un numero para la comparacion: "))
  n2 = int(input("Ingrese otro numero: "))

  if Max_or_Min(n1,n2)>-1 and Max_or_Min(n1,n2)<2:
     
     max = n1
     min = n2
  else:
     
     max = n2
     min = n1
  
  Imprimir_inf(max,min)

  for i in range(nrepeats-2):
     
    print("\n", "Leyendo... N° ",i+3,"\n")
    n1 = int(input("Ingrese un numero para la comparacion: "))

    if(Max_or_Min(max,n1)==1 and Max_or_Min(min,n1)==1):
     min=n1
     Imprimir_inf(max,min)

    elif(Max_or_Min(n1,max)==1):
      max=n1 
      Imprimir_inf(max,min)

    else: 
      Imprimir_inf(max,min)

elif(nrepeats==2):

  n1 = int(input("Ingrese un numero para la comparacion: "))
  n2 = int(input("Ingrese otro numero: "))
  Imprimir_inf(n1,n2)

elif(nrepeats<=1):

  print("Error N° INVALIDO")
