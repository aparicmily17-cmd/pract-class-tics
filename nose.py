#programa para calcular áreas
#Área cuadrado; lado x lado
print("Área de un cuadrado")
lado=float(input("ingresas lado"))
areaCuadrado=lado*lado
print ("El área es"), areaCuadrado
print(f'El área es {areaCuadrado}')
#Área de un triangulo
#(Base x Altura)/2
print("Área de un triangulo")
base=float(input("ingresa base"))
altura=float(input("ingresa altura"))
areaTriangulo=(base*altura)/2
print ("El área del triangulo es"), areaTriangulo
print(f'"El área es{areaTriangulo}')
#Área de un trapecio 
#base mayor+base menor/2 * altura
print("Área de un trapecio")
baseMayor=float(input("Ingresa base mayor"))
baseMenor=float(input("Ingresa base menor"))
altura=float(input("ingresa altura"))
areaTrapecio=(baseMayor+baseMenor)/2*altura
print("El área del trapecio es:"), areaTrapecio
print(f'El árera es{areaTrapecio}')