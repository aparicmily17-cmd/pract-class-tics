#Programa
print("////////////////////////////////")
calificaciones=float(input("Dame tu calificación:  "))
if calificaciones==10:
    print("Excelente")
elif califificaciones==9:
    print ("Muy bien")
elif calificaciones==8:
    print("Bien")
elif calificaciones==7:
    print ("Puedes Mejorar")
elif calificaciones==6:
    print("Puedes hacerlo mejor")
elif calificaciones==5:
    print("Muy Mal")
print ("////////////////////////////////////")
#Temperaturas
temp=float(input("Coloca tu temperatura:  "))
if temp==40:
    print("Hace mucho calor")
elif temp>=30 and temp<40:
    print("Esta templado")
elif temp>=20 and temp<30:
    print ("Esta fresco")
elif temp<=10 and temp<20:
    print("Hace Frio")
else:
    print("No valido")
print("//////////////////////////////")    
#Solicitar sexo y edad
sexo=input("Coloca tu edad")
edad=int(input("Coloca tu edad"))
if sexo=="Hobre" and edad>=18:
    print("Puedes sacar tu cartilla militar")
else:
    print("No puedes sacar cartilla")