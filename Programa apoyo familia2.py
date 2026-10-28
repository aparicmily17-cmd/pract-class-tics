#Programa apoyo familia
sexo=(input("Ingresa tu sexo: "))
cantHijos=float(int("Ingresa cantidad de hijos: "))
estCivil=(input("Ingresa tu estado civil: "))
edad=float(int("Ingrsa tu edad: "))
if sexo=="Mujer" and edad<18 and cantHijos>=1 :
    print("Eres mujer, tienes",cantHijos,"hijos y eres menor de edad entonces el apoyo será de $300")
elif sexo=="Mujer" and edad<18 and cantHijos>1:
   print("Eres mujer, tienes",cantHijos("hijos y eres mayor de edad entonces el apoyo será de $1500"))
elif sexo=="Mujer" and cantHijos>1 and edad>=18:
    print ("Eres mujer, tienes",cantHijos,"hijos ya eres mayor de edad entonces tu apoyo será de 500")
elif sexo=="Hombre"  and estCivil=="Soltero" and cantHijos>=1:
    print ("Eres hombre, tienes",cantHijos,"hijos y estas soltero, tu apoyo será de $780")
else: 
    print("Error") 