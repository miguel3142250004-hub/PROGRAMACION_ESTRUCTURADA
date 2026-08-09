import funciones
from historial_precios import crud


def menuHistorial():
    funciones.borrarPantalla()
    print("\n\t\t...:::: HISTORIAL DE PRECIOS ::::...\n")
    opcion = input("\n\t1.- Mostrar todo\n\t2.- Buscar por juego\n\t3.- Actualizar registro\n\t4.- Eliminar registro\n\t5.- Vaciar\n\t6.- Regresar al menu principal\n\t\tEscribe una opcion: ").strip()
    return opcion


def mostrarHistorial(conexionBD):
    print("\n\t\t...:::: HISTORIAL COMPLETO ::::...\n")
    historialBD = crud.consultar(conexionBD)
    if len(historialBD) > 0:
        print(f"\t{'ID':<5}{'Juego':<25}{'Plataforma':<15}{'Antes':<10}{'Fecha anterior':<17}{'Despues':<10}{'Tendencia':<10}{'Fecha cambio'}")
        for h in historialBD:
            diferencia = h[4] - h[3]   # expresion algoritmica
            if diferencia < 0:
                tendencia = "BAJO"
            elif diferencia > 0:
                tendencia = "SUBIO"
            else:
                tendencia = "IGUAL"
            print(f"\t{h[0]:<5}{h[1]:<25}{h[2]:<15}${h[3]:<9.2f}{str(h[6]):<17}${h[4]:<9.2f}{tendencia:<10}{h[5]}")
        funciones.espereTecla()
    else:
        input("...¡No hay historial registrado todavia!...")


def buscarHistorialPorJuego(conexionBD):
    print("\n\t\t...:::: BUSCAR HISTORIAL POR JUEGO ::::...\n")
    nombre = input("Nombre del juego: ").upper().strip()
    resultados = crud.buscarPorJuego(nombre, conexionBD)
    if len(resultados) > 0:
        for h in resultados:
            print(f"\t{h[6]} | {h[1]} en {h[2]}: ${h[3]:.2f} -> ${h[4]:.2f} ({h[5]})")
        funciones.espereTecla()
    else:
        input("...¡No hay historial para ese juego!...")


def actualizarHistorial(conexionBD):
    print("\n\t\t...:::: CORREGIR REGISTRO DE HISTORIAL ::::...\n")
    idHistorial = input("ID del registro a corregir: ").strip()
    if idHistorial.isdigit():
        precioAnterior = input("Precio anterior correcto: ").strip()
        precioNuevo = input("Precio nuevo correcto: ").strip()
        if funciones.validarPrecio(precioAnterior) and funciones.validarPrecio(precioNuevo):
            respuesta = crud.actualizar(int(idHistorial), float(precioAnterior), float(precioNuevo), conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
        else:
            funciones.opcionInvalida()
    else:
        funciones.opcionInvalida()


def eliminarHistorial(conexionBD):
    print("\n\t\t...:::: ELIMINAR REGISTRO DE HISTORIAL ::::...\n")
    idHistorial = input("ID del registro a eliminar: ").strip()
    if idHistorial.isdigit():
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas eliminar este registro (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crud.eliminar(int(idHistorial), conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        funciones.opcionInvalida()


def vaciarHistorial(conexionBD):
    historialBD = crud.consultar(conexionBD)
    if len(historialBD) > 0:
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas borrar TODO el historial (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crud.vaciar(conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No hay historial que borrar!...")
