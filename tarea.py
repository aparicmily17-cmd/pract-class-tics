#solicitar cadena
palabra=input("Escribe algo")
letra=input("Escrube una letra")
if letra in palabra:
    print("La letra si esta en la palabra")
else:
    print("La letra no esta en la palabra")
    cant=palabra lower().count(letra)
    print(f"la letra aparece{cant}veces")
    print("La letra aparece",cant "veces")
palaNew=palabra.replace(letra,"x")
cantLetra=len(palabra)
if len(palabra)>5:
    print("Tiene más de 5")
else:
    print("Tiene menos de 5 letras")