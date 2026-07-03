'''
Crear un proyecto que permita gestionar (administrar) peliculas. Colocar un menu de opciones: Agregar, Borrar, Modificar, Mostrar, Buscar, Limpiar una lista de peliculas.

Notas: 
1.- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2.- Utilizar dict para almacenar los atributos (nombre,categoria,clasificacion,genero,idioma) de peliculas
3.- Utilizar o implementar BD relacional con MySQL para guardar la información

'''
from peliculas import peliculas
import funciones

#Conexion con la BD
conexionBD=funciones.conetar()

opc=""

while opc!="7":
    funciones.borrarPantalla()
    opc=peliculas.menuPrincial()
    match opc:
        case "1":
            funciones.borrarPantalla()
            peliculas.agregarPeliculas(conexionBD)
        case "2":
            funciones.borrarPantalla()
            peliculas.borrarPeliculas(conexionBD)
        case "3":
            funciones.borrarPantalla()
            peliculas.modificarPeliculas(conexionBD)
        case "4":
            funciones.borrarPantalla()
            peliculas.mostrarPeliculas(conexionBD)
        case "5":
            funciones.borrarPantalla()
            peliculas.buscarPeliculas(conexionBD)
        case "6":
            funciones.borrarPantalla()
            peliculas.limpiarPeliculas(conexionBD)
        case "7":
            funciones.borrarPantalla()
            funciones.terminarSistema()
        case _:
            funciones.opcionInvalida()
