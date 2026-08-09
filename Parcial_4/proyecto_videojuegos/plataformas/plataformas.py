import funciones
from plataformas import crud


def menuPlataformas():
    funciones.borrarPantalla()
    print("\n\t\t...:::: GESTION DE PLATAFORMAS ::::...\n")
    opcion = input("\n\t1.- Agregar\n\t2.- Mostrar\n\t3.- Buscar\n\t4.- Actualizar\n\t5.- Eliminar\n\t6.- Vaciar\n\t7.- Regresar al menu principal\n\t\tEscribe una opcion: ").strip()
    return opcion


def agregarPlataforma(conexionBD):
    print("\n\t\t...:::: AGREGAR PLATAFORMA ::::...\n")
    nombre = input("Nombre de la plataforma (ej. Steam, Epic Games, GOG): ").strip()
    while not funciones.validarTexto(nombre):
        print("\n...¡El nombre solo debe contener letras!...")
        nombre = input("Nombre de la plataforma: ").strip()

    url = input("URL de la tienda (ej. https://store.steampowered.com): ").strip()
    while not funciones.validarURL(url):
        print("\n...¡URL invalida, debe iniciar con http:// o https://!...")
        url = input("URL de la tienda: ").strip()

    datosPlataforma = {"nombre": nombre.title(), "url": url}
    respuesta = crud.insertar(datosPlataforma, conexionBD)
    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNoExitosa()


def mostrarPlataformas(conexionBD):
    print("\n\t\t...:::: MOSTRAR PLATAFORMAS ::::...\n")
    plataformasBD = crud.consultar(conexionBD)
    if len(plataformasBD) > 0:
        print(f"\t{'ID':<5}{'Nombre':<15}{'URL'}")
        for p in plataformasBD:
            print(f"\t{p[0]:<5}{p[1]:<15}{p[2]}")
        funciones.espereTecla()
    else:
        input("...¡No hay plataformas registradas!...")


def buscarPlataforma(conexionBD):
    print("\n\t\t...:::: BUSCAR PLATAFORMA ::::...\n")
    nombre = input("Nombre de la plataforma: ").strip()
    resultados = crud.buscar(nombre, conexionBD)
    if len(resultados) > 0:
        for p in resultados:
            print(f"\t{p[0]}\t{p[1]}\t{p[2]}")
        funciones.espereTecla()
    else:
        input("...¡No se encontro esa plataforma!...")


def actualizarPlataforma(conexionBD):
    print("\n\t\t...:::: ACTUALIZAR PLATAFORMA ::::...\n")
    idPlataforma = input("ID de la plataforma: ").strip()
    if idPlataforma.isdigit():
        nombre = input("Nuevo nombre: ").strip()
        while not funciones.validarTexto(nombre):
            print("\n...¡El nombre solo debe contener letras!...")
            nombre = input("Nuevo nombre: ").strip()
        url = input("Nueva URL: ").strip()
        while not funciones.validarURL(url):
            print("\n...¡URL invalida!...")
            url = input("Nueva URL: ").strip()

        datosPlataforma = {"nombre": nombre.title(), "url": url}
        respuesta = crud.actualizar(int(idPlataforma), datosPlataforma, conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()
    else:
        funciones.opcionInvalida()


def eliminarPlataforma(conexionBD):
    print("\n\t\t...:::: ELIMINAR PLATAFORMA ::::...\n")
    idPlataforma = input("ID de la plataforma: ").strip()
    if idPlataforma.isdigit():
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas eliminar esta plataforma y sus precios asociados (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crud.eliminar(int(idPlataforma), conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        funciones.opcionInvalida()


def vaciarPlataformas(conexionBD):
    plataformasBD = crud.consultar(conexionBD)
    if len(plataformasBD) > 0:
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas borrar TODAS las plataformas (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crud.vaciar(conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No hay plataformas que borrar!...")
