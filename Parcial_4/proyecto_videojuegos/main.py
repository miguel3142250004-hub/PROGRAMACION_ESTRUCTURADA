'''
Proyecto Final - Comparador de Precios de Videojuegos de PC
Problematica: un mismo videojuego de PC puede tener precios distintos
segun la tienda digital donde se compre (Steam, Epic Games o GOG).
Este sistema permite registrar juegos, plataformas y precios, comparar
cual es la opcion mas barata para un juego, y llevar un historial de
como han cambiado esos precios a lo largo del tiempo.

Notas:
1.- Se utilizan funciones y modulos separados: un paquete por cada tabla
    (juegos, plataformas, precios, historial_precios), cada uno con su
    propio modulo de acceso a datos (crud.py) y su modulo de logica/menu.
2.- Se utilizan diccionarios para agrupar los atributos de cada registro
    antes de mandarlos a la base de datos.
3.- Se implementa una BD relacional en MySQL con 4 tablas relacionadas
    por llaves foraneas (juegos, plataformas, precios, historial_precios).
'''
import funciones
from juegos import juegos
from plataformas import plataformas
from precios import precios
from historial_precios import historial_precios

# Conexion con la BD
conexionBD = funciones.conectar()

opc = ""

while opc != "5":
    funciones.borrarPantalla()
    print("\n\t\t...:::: COMPARADOR DE PRECIOS DE VIDEOJUEGOS ::::...\n")
    opc = input("\n\t1.- Gestionar Juegos\n\t2.- Gestionar Plataformas\n\t3.- Gestionar Precios\n\t4.- Ver Historial de Precios\n\t5.- Salir\n\t\tEscribe una opcion: ").strip()

    match opc:
        case "1":
            opcJuegos = ""
            while opcJuegos != "7":
                opcJuegos = juegos.menuJuegos()
                match opcJuegos:
                    case "1":
                        funciones.borrarPantalla()
                        juegos.agregarJuego(conexionBD)
                    case "2":
                        funciones.borrarPantalla()
                        juegos.mostrarJuegos(conexionBD)
                    case "3":
                        funciones.borrarPantalla()
                        juegos.buscarJuego(conexionBD)
                    case "4":
                        funciones.borrarPantalla()
                        juegos.actualizarJuego(conexionBD)
                    case "5":
                        funciones.borrarPantalla()
                        juegos.eliminarJuego(conexionBD)
                    case "6":
                        funciones.borrarPantalla()
                        juegos.vaciarJuegos(conexionBD)
                    case "7":
                        pass
                    case _:
                        funciones.opcionInvalida()

        case "2":
            opcPlataformas = ""
            while opcPlataformas != "7":
                opcPlataformas = plataformas.menuPlataformas()
                match opcPlataformas:
                    case "1":
                        funciones.borrarPantalla()
                        plataformas.agregarPlataforma(conexionBD)
                    case "2":
                        funciones.borrarPantalla()
                        plataformas.mostrarPlataformas(conexionBD)
                    case "3":
                        funciones.borrarPantalla()
                        plataformas.buscarPlataforma(conexionBD)
                    case "4":
                        funciones.borrarPantalla()
                        plataformas.actualizarPlataforma(conexionBD)
                    case "5":
                        funciones.borrarPantalla()
                        plataformas.eliminarPlataforma(conexionBD)
                    case "6":
                        funciones.borrarPantalla()
                        plataformas.vaciarPlataformas(conexionBD)
                    case "7":
                        pass
                    case _:
                        funciones.opcionInvalida()

        case "3":
            opcPrecios = ""
            while opcPrecios != "8":
                opcPrecios = precios.menuPrecios()
                match opcPrecios:
                    case "1":
                        funciones.borrarPantalla()
                        precios.agregarPrecio(conexionBD)
                    case "2":
                        funciones.borrarPantalla()
                        precios.mostrarPrecios(conexionBD)
                    case "3":
                        funciones.borrarPantalla()
                        precios.buscarPrecioPorJuego(conexionBD)
                    case "4":
                        funciones.borrarPantalla()
                        precios.actualizarPrecio(conexionBD)
                    case "5":
                        funciones.borrarPantalla()
                        precios.eliminarPrecio(conexionBD)
                    case "6":
                        funciones.borrarPantalla()
                        precios.vaciarPrecios(conexionBD)
                    case "7":
                        funciones.borrarPantalla()
                        precios.generarReportePrecios(conexionBD)
                    case "8":
                        pass
                    case _:
                        funciones.opcionInvalida()

        case "4":
            opcHistorial = ""
            while opcHistorial != "6":
                opcHistorial = historial_precios.menuHistorial()
                match opcHistorial:
                    case "1":
                        funciones.borrarPantalla()
                        historial_precios.mostrarHistorial(conexionBD)
                    case "2":
                        funciones.borrarPantalla()
                        historial_precios.buscarHistorialPorJuego(conexionBD)
                    case "3":
                        funciones.borrarPantalla()
                        historial_precios.actualizarHistorial(conexionBD)
                    case "4":
                        funciones.borrarPantalla()
                        historial_precios.eliminarHistorial(conexionBD)
                    case "5":
                        funciones.borrarPantalla()
                        historial_precios.vaciarHistorial(conexionBD)
                    case "6":
                        pass
                    case _:
                        funciones.opcionInvalida()

        case "5":
            funciones.borrarPantalla()
            funciones.terminarSistema()

        case _:
            funciones.opcionInvalida()
