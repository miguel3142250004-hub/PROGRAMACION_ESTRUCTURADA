import funciones
from peliculas import crud
      
def menuPrincial():
    print("\n\t\t...:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion

def agregarPeliculas(conexionBD):
    print("\n\t\t...:::: AGREGAR PELICULAS ::::...\n")
    peli=input("Introducir el nombre de la pelicula: ").upper().strip()
    respuesta=crud.insertar(peli,conexionBD)
    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNoExitosa()    

def mostrarPeliculas(conexionBD):
    print("\n\t\t...:::: MOSTRAR PELICULAS ::::...\n")
    pelis=crud.consultar(conexionBD)
    if len(pelis)>0:
        print("\tCodigo\t\tPelicula\n")
        for i in pelis:
          print(f"\t{i[0]}\t\t{i[1]}")
          funciones.espereTecla()
    else:        
      input("...¡No hay peliculas que mostrar!...")       
    
def limpiarPeliculas(conexionBD):
    pelis=crud.consultar(conexionBD)
    if len(pelis)>0:
        opc=""
        while opc!="si" and opc!="no":
            opc=input("¿Deseas borrar TODAS las pelicula (Si/No)? ").lower().strip()
        if opc=="si":       
            respuesta=crud.vaciar(conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()       
    else:        
      input("...¡No hay peliculas que borrar!...") 
    funciones.espereTecla()  
        
# def buscarPeliculas(pelis):
#     print("\n\t\t...:::: BUSCAR PELICULAS ::::...\n")
#     peli=input("Escribir el nombre de la pelicula: ").upper().strip()
#     if peli in pelis:
#         print("\tCodigo\t\tPelicula\n")
#         for i in range(0,len(pelis)):
#           if peli==pelis[i]:
#              print(f"{i+1}\t\t{pelis[i]}")
#         funciones.espereTecla()
#     else:
#         input("...¡No exite la pelicula que estas buscando, verifique!...")

# def borrarPeliculas(pelis):
#     posiciones=[]
#     print("\n\t\t...:::: BORRAR PELICULAS ::::...\n")
#     peli=input("Escribir el nombre de la pelicula: ").upper().strip()
#     if peli in pelis:
#         for i in range(0,len(pelis)):
#             if peli==pelis[i]:
#                 opc=""
#                 while opc!="si" and opc!="no":
#                   opc=input("¿Deseas borrar la pelicula (Si/No)? ").lower().strip()
#                 if opc=="si":
#                   posiciones.append(i)
#         if len(posiciones)>0:
#             for i in range(0,len(posiciones)):
#                 pelis.remove(peli)
#             funciones.accionExitosa()
#     else:
#         input("...¡No exite la pelicula que estas buscando, verifique!...")
        
# def modificarPeliculas(pelis):
    # posiciones=[]
    # print("\n\t\t...:::: MODIFICAR PELICULAS ::::...\n")
    # peli=input("Escribir el nombre de la pelicula: ").upper().strip()
    # if peli in pelis:
    #     for i in range(0,len(pelis)):
    #         if peli==pelis[i]:
    #             opc=""
    #             while opc!="si" and opc!="no":
    #               opc=input("¿Deseas modificar la pelicula (Si/No)? ").lower().strip()
    #             if opc=="si":
    #               pelis[i]=input("Escribe el nuevo nombre: ").upper().strip()
    #               funciones.accionExitosa()
    # else:
    #     input("...¡No exite la pelicula que estas buscando, verifique!...")