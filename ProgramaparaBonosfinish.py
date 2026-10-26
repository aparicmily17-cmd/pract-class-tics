#Programa para Calcular Bonos
print(input("Ingresa tu nombre: "))
pagoHora=float(input("Ingresa tu pago por horas: $"))
horasTra=float(input("Ingresa tus horas trabajadas al mes: "))
sueldo=pagoHora*horasTra
bono=sueldo+500
if sueldo>=100 and sueldo<=300:
    print("Tu sueldo es de:$",sueldo)
    print("Tu sueldo con bono es de:$",bono) 
elif sueldo>300 and sueldo<=1500:
    print("Tu sueldo es de:$",sueldo)
    print("Tu sueldo con bono es de:$ ",bono)
elif sueldo>1500 and sueldo<=3000:
    print("Tu sueldo es de:$",sueldo)
    print ("Tu sueldo con bono es de:$ ",bono)
elif sueldo>3000 and sueldo<=8000:
    print("Tu sueldo es de:$ ",sueldo)
    print("Tu sueldo con bono:$ ",bono)
elif sueldo>8000:
    print("Tu sueldo sueldo es de:$ ",sueldo)
    print("Tu sueldo con bono es de:$10000")
else:
    print("No válido")