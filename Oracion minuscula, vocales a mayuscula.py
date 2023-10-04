import os
import re
'''
Dada una oración escrita toda en minúscula, 
convierta cada vocal existente en esta por su 
respectiva mayúscula.

'''

#Función para modificar las oraciones
def vocals_upper(txt):
 new_txt = ""
 for i in txt:
   if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
    i = i.upper()
    new_txt = new_txt + i
   else:
    new_txt = new_txt + i
 return new_txt

def menu():
 val = True
 val2 = True
 while(val):
  val2 = True 
  txt = input("Ingrese el texto a modificar: ")

  '''
    re.fullmatch, compara los caracteres de la cadena con el rango ingresado (A-Z) (a-z), incluye un máximo 
    número de caracteres de 280 y considera los caracteres acentuados y la ñ
  
  '''

  if(re.fullmatch(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ ]{1,280}", txt)):
   txt = txt.lower()
   txt = vocals_upper(txt)
   print(txt)
   while(val2):
    opc = input("Desea modificar otro texto? (Y/N): ")
    if(opc=="Y" or opc=="y"):
     val = True
     val2 = False
     os.system("cls")
    elif(opc=="N" or opc=="n"):
     val = False
     val2 = False
     print("Gracias por usar este programa, mi bro")
    else:
     print("Por favor ingrese Y/N")  
  else:
   print("No se admiten numeros ni caracteres especiales. Max 280 caracteres")

menu()
