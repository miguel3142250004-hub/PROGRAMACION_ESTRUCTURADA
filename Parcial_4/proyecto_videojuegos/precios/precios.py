import funciones
from precios import crud
from historial_precios import crud as crudHistorial


def menuPrecios():
    funciones.borrarPantalla()
    print("\n\t\t...:::: GESTION DE PRECIOS ::::...\n")
    opcion = input("\n\t1.- Agregar\n\t2.- Mostrar comparativa\n\t3.- Buscar mejor precio por juego\n\t4.- Actualizar\n\t5.- Eliminar\n\t6.- Vaciar\n\t7.- Generar reporte (.txt)\n\t8.- Regresar al menu principal\n\t\tEscribe una opcion: ").strip()
    return opcion


def agregarPrecio(conexionBD):
    print("\n\t\t...:::: AGREGAR PRECIO ::::...\n")
    juegosBD, plataformasBD = crud.listarJuegosPlataformas(conexionBD)

    if len(juegosBD) == 0 or len(plataformasBD) == 0:
        input("...¡Primero registra al menos un juego (y verifica que existan plataformas)!...")
        return

    print("Juegos disponibles:")
    for j in juegosBD:
        print(f"\t{j[0]} - {j[1]}")
    idJuego = input("\nID del juego: ").strip()

    print("\nPlataformas disponibles:")
    for p in plataformasBD:
        print(f"\t{p[0]} - {p[1]}")
    idPlataforma = input("\nID de la plataforma: ").strip()

    precio = input("Precio (ej. 599.99): ").strip()
    while not funciones.validarPrecio(precio):
        print("\n...¡Precio invalido, usa solo numeros y un punto decimal!...")
        precio = input("Precio: ").strip()

    moneda = input(f"Moneda {funciones.MONEDAS_VALIDAS} [USD]: ").upper().strip()
    if moneda == "" or moneda not in funciones.MONEDAS_VALIDAS:
        moneda = "USD"

    descuento = input("Descuento % (0 si no aplica): ").strip()
    descuento = int(descuento) if descuento.isdigit() else 0

    if idJuego.isdigit() and idPlataforma.isdigit():
        datosPrecio = {
            "id_juego": int(idJuego),
            "id_plataforma": int(idPlataforma),
            "precio": float(precio),
            "moneda": moneda,
            "descuento": descuento
        }
        respuesta = crud.insertar(datosPrecio, conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()
    else:
        funciones.opcionInvalida()


def mostrarPrecios(conexionBD):
    print("\n\t\t...:::: COMPARATIVA DE PRECIOS ::::...\n")
    preciosBD = crud.consultar(conexionBD)
    if len(preciosBD) > 0:
        print(f"\t{'ID':<5}{'Juego':<25}{'Plataforma':<15}{'Precio final':<14}{'Descuento':<10}{'Actualizado'}")
        for p in preciosBD:
            print(f"\t{p[0]:<5}{p[1]:<25}{p[2]:<15}${p[7]:<13.2f}{p[5]}%{'':<7}{p[6]}")
        funciones.espereTecla()
    else:
        input("...¡No hay precios registrados!...")


def buscarPrecioPorJuego(conexionBD):
    print("\n\t\t...:::: BUSCAR MEJOR PRECIO ::::...\n")
    nombre = input("Nombre del juego: ").upper().strip()
    resultados = crud.buscarPorJuego(nombre, conexionBD)
    if len(resultados) > 0:
        print(f"\t{'Juego':<25}{'Plataforma':<15}{'Precio':<12}{'Descuento':<12}{'Precio final'}")
        for r in resultados:
            print(f"\t{r[1]:<25}{r[2]:<15}${r[3]:<11.2f}{r[5]}%{'':<9}${r[7]:.2f}")
        mejorOpcion = resultados[0]   # ya viene ordenado por precio_final
        print(f"\n\t...La mejor opcion es {mejorOpcion[2]} con ${mejorOpcion[7]:.2f}...")
        funciones.espereTecla()
    else:
        input("...¡No se encontraron precios para ese juego!...")


def actualizarPrecio(conexionBD):
    print("\n\t\t...:::: ACTUALIZAR PRECIO ::::...\n")
    idPrecio = input("ID del precio a actualizar: ").strip()
    if idPrecio.isdigit():
        precioAnterior = crud.obtenerPrecioActual(int(idPrecio), conexionBD)
        if precioAnterior != None:
            nuevoPrecio = input(f"Precio actual: ${precioAnterior} - Nuevo precio: ").strip()
            while not funciones.validarPrecio(nuevoPrecio):
                print("\n...¡Precio invalido!...")
                nuevoPrecio = input("Nuevo precio: ").strip()

            respuesta = crud.actualizar(int(idPrecio), float(nuevoPrecio), conexionBD)
            if respuesta:
                # Se deja constancia del cambio en la tabla historial_precios
                crudHistorial.insertar(int(idPrecio), float(precioAnterior), float(nuevoPrecio), conexionBD)
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
        else:
            input("...¡No existe un precio con ese ID!...")
    else:
        funciones.opcionInvalida()


def eliminarPrecio(conexionBD):
    print("\n\t\t...:::: ELIMINAR PRECIO ::::...\n")
    idPrecio = input("ID del precio a eliminar: ").strip()
    if idPrecio.isdigit():
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas eliminar este precio (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crud.eliminar(int(idPrecio), conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        funciones.opcionInvalida()


def vaciarPrecios(conexionBD):
    preciosBD = crud.consultar(conexionBD)
    if len(preciosBD) > 0:
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas borrar TODOS los precios (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crud.vaciar(conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No hay precios que borrar!...")


def generarReportePrecios(conexionBD):
    print("\n\t\t...:::: GENERAR REPORTE DE PRECIOS ::::...\n")
    preciosBD = crud.consultar(conexionBD)
    if len(preciosBD) > 0:
        datosReporte = [(fila[1], fila[2], fila[7]) for fila in preciosBD]   # usa el precio con descuento
        respuesta = funciones.generarReporteTxt(datosReporte)
        if respuesta:
            input("...¡Reporte generado con exito! Revisa el archivo 'reporte_precios.txt' en la carpeta del proyecto!...")
        else:
            funciones.accionNoExitosa()
    else:
        input("...¡No hay precios registrados para generar un reporte!...")
