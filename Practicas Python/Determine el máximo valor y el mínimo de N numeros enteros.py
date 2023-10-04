#Determine el máximo valor y el mínimo valor de N números enteros (Forma 1)

def Max_or_Min(n1, n2):
  if n1 > n2:
    return 1
  elif n1 < n2:
    return 2
  else:
    return 0

val = "Y"
max = 0
min = 0

print("Bienvenido a este comparador de numeros","\n")
n1 = int(input("Ingrese un numero para la comparacion: "))
n2 = int(input("Ingrese otro numero: "))

if(Max_or_Min(n1, n2)==1):
  max = n1
  min = n2
  print("El mayor es ", max, "Y el menor ", min)

elif(Max_or_Min(n1, n2)==2):
  max = n2
  min = n1
  print("El mayor es ", max, "Y el menor ", min)

else:
  print("Ambos numeros son iguales")
  max = n1
  min = n2

while(val != 'N' or val != 'n'):
  val = str(input("¿Desea continuar? (Y/N) "))

  if(val == "y" or val == "Y"):
   n1 = int(input("Ingrese un numero para la comparacion: "))
   if(Max_or_Min(max,n1)==1 and Max_or_Min(min,n1)==1):
     min=n1
     print("El mayor hasta ahora es ", max, "Y el menor ", min)
   elif(Max_or_Min(n1,max)==1):
     max=n1 
     print("El mayor hasta ahora es ", max, "Y el menor ", min)
   else: 
     print("El mayor hasta ahora es ", max, "Y el menor ", min)
  elif(val == "N" or val== "n"):
    print("Gracias por usar este programa")
    break
  else:
     pass