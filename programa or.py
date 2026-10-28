#programa familiar or
parentesco=input("¿Qué eres mio?")
if parentesco=="Papá" or parentesco=="Mamá" or parentesco=="Hermano" or parentesco=="Hermana":
    print("Eres de mi familia")
else:
    print("No eres de mi familia")
print("-------------------------------------------------------------------------------")
#Programa entrar al concierto
edad=float(input("Ingresa tu edad: "))
permiso=input("¿Tienes permiso de tus padres? ")
acom=input("¿Vienes acompañado de un mayor de edad?")
if edad>=18 or permiso=="Si":
    print("Puedes entrar al concierto")
if edad>=18 or acom=="Si":
    print("Puedes entrar al concierto")
else:
    print("No puedes entrar al concierto")