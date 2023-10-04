#Buscador de palabras que comiencen con una letra en especifico

letter_pass = True
text_pass = True
print("Bienvenido a este programa de busqueda de coincidencias en un texto.")
while(letter_pass):
   
 texto = input("Ingresa el texto a analizar: ")
 texto = texto.lower()
 lista_palabras = texto.split(" ")
 for i in lista_palabras:
  if(not i.isalpha()):
    text_pass = True
    break
  else:
   text_pass = False
 
 if(text_pass == False):
  
  while(letter_pass):
     
   letra = input("Ingresa la letra: ")
   if(letra.isalpha() and len(letra)<2):
    letter_pass = False
    letra = letra.lower()
    coincidence_counter = 0
    lista_palabras = sorted(lista_palabras)

    for i in lista_palabras:
     if(not i.find(letra)):
      print(i)
      coincidence_counter = coincidence_counter + 1

    print("Se encontraron un total de ", coincidence_counter, "palabras que cumplen con el parametro ingresado" )  

   else:
    print("ERROR, NO SE PERMITEN CARACTERES NO ALFABETICOS, SOLO UNA LETRA PARA LA BUSQUEDA")
    
 else:
   print("ERROR, NO SE PERMITEN CARACTERES NO ALFABETICOS")    
