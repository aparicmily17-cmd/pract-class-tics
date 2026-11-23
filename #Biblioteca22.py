#Biblioteca
libros=[]
usuarios=[]
prestamos=[]
opcion=""
while opcion!="7":
    print("//////////Biblioteca//////////")
    print("1.-Registrar un libro")
    print("2.-Consultar un libro")
    print("3.-Registrar usuario")
    print("4.-Prestar libro")
    print("5.-Devolver libro")
    print("6.-Ver reporte")
    print("7.-Salir")
    opcion=input("Quiero: ")
    if opcion=="1":
        print("////////////////Registrar Libro////////////////")
        Titulo=input("Inserta Titulo del libro: ")
        Autor=input("Inserta Autor del libro: ")
        Editorial=input("Inserta Editorial: ")
        año=input("Inserta Año del libro: ")
        Categoria=input("Inserta Categoria del libro: ")
        libros.append([Titulo,Autor,Editorial,año,Categoria,"Disponible"])
        print("¡¡Libro guaradado!!")
    elif opcion=="2":
        print("////////////////Buscar Libro////////////////")
        buscar=input("Escribe titulo, autor o categoria del libro que deseas buscar: ")
        for libro in libros:
            if buscar.lower()in libro[0].lower() or buscar.lower()in libro[1].lower()in libro[4].lower():
                print(libro)
            elif opcion=="3":
                print("////////////////Reguistro de Usuarios////////////////")
                nombre=input("Ingresa tu nombre completo: ")
                edad=int(input("Ingresa tu edad: "))
                correo=input("Ingresa tu correo electronico: ")
                tel=int(input("Ingresa tu numero de telefono: "))
                usuarios.append([nombre,edad,correo,tel])
                print("¡¡Usuario Registrado!!")
            elif opcion=="4":
                print("////////////////Prestar Libros////////////////")
                titulo=input("¿Qué libro quieres prestar?: ")
                for libro in libros:
                    if libro[0].lower()==titulo.lower():
                        