#listas
alumnos=["Juanito","Angelito"]
#Diccionarios
alumno1={
    "Nombre":"Juanito",
    "edad":15,
    "promedio":10
}
alumno2={
    "Nombre":"Angelito",
    "Edad":18,
    "promedio":10
}
#Consultar valores
#Forma 1
print("Nombre :",alumno1["Nombre"])
#Forma 2
print("Nombre :", alumno1.get("Nombre"))
#Modificar algun campo
alumno1["Nombre"]="Pedrito"
print("Nombre: ",alumno1.get("Nombre"))