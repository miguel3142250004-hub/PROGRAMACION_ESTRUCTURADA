import funciones
from juegos import crud


def menuJuegos():
    funciones.borrarPantalla()
    print("\n\t\t...:::: GESTION DE JUEGOS ::::...\n")
    opcion = input("\n\t1.- Agregar\n\t2.- Mostrar\n\t3.- Buscar\n\t4.- Actualizar\n\t5.- Eliminar\n\t6.- Vaciar\n\t7.- Regresar al menu principal\n\t\tEscribe una opcion: ").strip()
    return opcion


def agregarJuego(conexionBD):
    print("\n\t\t...:::: AGREGAR JUEGO ::::...\n")
    nombre = input("Nombre del juego: ").upper().strip()

    genero = input("Genero (Accion, RPG, Estrategia, etc): ").upper().strip()
    while not funciones.validarTexto(genero):
        print("\n...¡El genero solo debe contener letras!...")
        genero = input("Genero: ").upper().strip()

    desarrollador = input("Desarrollador: ").upper().strip()

    anio = input("Año de lanzamiento (ej. 2023): ").strip()
    while not funciones.validarAnio(anio):
        print("\n...¡Año invalido, verifique el formato (1970-2030)!...")
        anio = input("Año de lanzamiento: ").strip()

    datosJuego = {"nombre": nombre, "genero": genero, "desarrollador": desarrollador, "anio": int(anio)}
    respuesta = crud.insertar(datosJuego, conexionBD)
    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNoExitosa()


def mostrarJuegos(conexionBD):
    print("\n\t\t...:::: MOSTRAR JUEGOS ::::...\n")
    juegosBD = crud.consultar(conexionBD)
    if len(juegosBD) > 0:
        print(f"\t{'ID':<5}{'Nombre':<30}{'Genero':<15}{'Desarrollador':<20}{'Año':<6}")
        for j in juegosBD:
            print(f"\t{j[0]:<5}{j[1]:<30}{j[2]:<15}{j[3]:<20}{j[4]:<6}")
        funciones.espereTecla()
    else:
        input("...¡No hay juegos registrados!...")


def buscarJuego(conexionBD):
    print("\n\t\t...:::: BUSCAR JUEGO ::::...\n")
    nombre = input("Nombre del juego a buscar: ").upper().strip()
    resultados = crud.buscar(nombre, conexionBD)
    if len(resultados) > 0:
        print(f"\t{'ID':<5}{'Nombre':<30}{'Genero':<15}{'Desarrollador':<20}{'Año':<6}")
        for j in resultados:
            print(f"\t{j[0]:<5}{j[1]:<30}{j[2]:<15}{j[3]:<20}{j[4]:<6}")
        funciones.espereTecla()
    else:
        input("...¡No se encontraron juegos con ese nombre!...")


def actualizarJuego(conexionBD):
    print("\n\t\t...:::: ACTUALIZAR JUEGO ::::...\n")
    idJuego = input("ID del juego a actualizar: ").strip()
    if idJuego.isdigit():
        nombre = input("Nuevo nombre: ").upper().strip()
        genero = input("Nuevo genero: ").upper().strip()
        while not funciones.validarTexto(genero):
            print("\n...¡El genero solo debe contener letras!...")
            genero = input("Nuevo genero: ").upper().strip()
        desarrollador = input("Nuevo desarrollador: ").upper().strip()
        anio = input("Nuevo año: ").strip()
        while not funciones.validarAnio(anio):
            print("\n...¡Año invalido!...")
            anio = input("Nuevo año: ").strip()

        datosJuego = {"nombre": nombre, "genero": genero, "desarrollador": desarrollador, "anio": int(anio)}
        respuesta = crud.actualizar(int(idJuego), datosJuego, conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()
    else:
        funciones.opcionInvalida()


def eliminarJuego(conexionBD):
    print("\n\t\t...:::: ELIMINAR JUEGO ::::...\n")
    idJuego = input("ID del juego a eliminar: ").strip()
    if idJuego.isdigit():
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas eliminar este juego, junto con sus precios asociados (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crud.eliminar(int(idJuego), conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        funciones.opcionInvalida()


def vaciarJuegos(conexionBD):
    juegosBD = crud.consultar(conexionBD)
    if len(juegosBD) > 0:
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas borrar TODOS los juegos (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crud.vaciar(conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No hay juegos que borrar!...")
