#Programa que agrega peliculas a una lista
peliculas=[]
#Preguntar cuantas peliculas
cantPeli=int(input("¿Cuántas peliculas vas a agregar?: "))
i=0
while i<cantPeli:
    peli=input("Ingresa la peli: ")
    peliculas.append(peli)
    print(peliculas)
    i=i+1
#Buscar peli en lista
peliBusq=input("¿Que pelicula buscas?")
if peliBusq in peliculas:
    print("Si está disponible")
else:
    print("No esta, pero dejame agragarla")
    peliculas.append(peliBusq)
    print(peliculas)
peliBorrar=input("¿Cuál quieres borrar?")
peliBorrar.remove(peliBorrar)
print(peliculas)

