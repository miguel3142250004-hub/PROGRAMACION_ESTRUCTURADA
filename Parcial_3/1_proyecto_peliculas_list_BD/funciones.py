import mysql.connector


def borrarPantalla():
    print("\033c")
    
def espereTecla():
    input("\n\t...¡Oprima cualquier tecla para continuar!...")
    
def opcionInvalida():
    input("\n\t...¡Opcion invalidad, por favor verifique !...")
    
def accionExitosa():
    input("\n\t...¡Accion Realizada con Exito !...")
    
def accionNoExitosa():
    input("\n\t...¡No fue posible realizar esta accion, intentalo mas tarde !...")    

def terminarSistema():
    input("\n\t\t...:::: GRACIAS POR UTILIZAR NUESTRO SISTEMA ::::...\n")

def conetar():
    try:
       conexion=mysql.connector.connect(
           host="127.0.0.1",
           user="root",
           password="",
           database="bd_peliculas_v1"
       ) 
       return conexion
    except:
        input("...¡Por el momento no es posible conectar el sistema o aplicacion con la Base de datos, intentalo mas tarde! ...")
        return None