#busqueda
nombres=["Angel","Karla","Luis","Mateo","María","Luis","Karla"]
print(f"Los nombres que se tienen son:")
print(nombres)
nombrBusq=input("¿Qué nombre deseas buscar?")
encontrado=False
contador=0
i=0
while i<len(nombres):
    if nombres[i]==nombrBusq:
        encontrado=True
        contador=contador+1
        print("Encontrado en la posición: ",i)
        i=o+1
        if encontrado==True:
            print("Nombre encontrado")
            print("Aparece",contador,"veces")
        else:
            print("Nombre no encontrado")