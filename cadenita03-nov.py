#Cadenita
nombre="Mily"
frase="no se jajaj"
print(nombre)
print(frase)
print("//////////////////////////////////////////////////////////")
#Mostrar el nombre mayus
print(nombre.upper())
print(frase.upper())
print("//////////////////////////////////////////////////////////")
#Mostrar en minusculas
print(frase.lower())
print("//////////////////////////////////////////////////////////")
#Obtener un carácter en una posicion
letra=frase[4] 
print(letra)
frase2="El-mundo-es-bonito"
print(frase2.split("-"))
nombreC="Emily García Aparicio"
print(nombreC.split(" "))
print("//////////////////////////////////////////////////////////")
#Dos primeras letras del nombre
letras1=nombreC[0:2]
print(letras1)
print("//////////////////////////////////////////////////////////")
#cambiar Frace
nuevaFrace=frase.replace("no se","si se")
print(nuevaFrace)
print("//////////////////////////////////////////////////////////")
#numero de caracter en una cadena
largoCad=len(nuevaFrace)
print(largoCad)