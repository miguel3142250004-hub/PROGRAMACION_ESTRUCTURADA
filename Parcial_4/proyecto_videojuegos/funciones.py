import re
from datetime import datetime
import mysql.connector

# ---------------- CONSTANTES ----------------
NOMBRE_BD = "bd_videojuegos"
MONEDAS_VALIDAS = ("USD", "MXN", "EUR")


# ---------------- UTILIDADES DE CONSOLA ----------------
def borrarPantalla():
    print("\033c")

def espereTecla():
    input("\n\t...¡Oprima cualquier tecla para continuar!...")

def opcionInvalida():
    input("\n\t...¡Opcion invalida, por favor verifique!...")

def accionExitosa():
    input("\n\t...¡Accion realizada con exito!...")

def accionNoExitosa():
    input("\n\t...¡No fue posible realizar esta accion, intentalo mas tarde!...")

def terminarSistema():
    input("\n\t\t...:::: GRACIAS POR UTILIZAR NUESTRO SISTEMA ::::...\n")


# ---------------- CONEXION A LA BASE DE DATOS ----------------
def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database=NOMBRE_BD
        )
        asegurarColumnaPrecioFinal(conexion)
        asegurarFechaAnterior(conexion)
        return conexion
    except Exception:
        input("...¡Por el momento no es posible conectar el sistema con la Base de Datos, intentalo mas tarde!...")
        return None


def asegurarColumnaPrecioFinal(conexion):
    """Agrega precio_final a instalaciones anteriores de la base de datos.

    La columna es generada por MySQL, por lo que siempre se vuelve a calcular
    cuando cambian el precio o el descuento.
    """
    cursor = conexion.cursor()
    cursor.execute("""
        select count(*)
        from information_schema.columns
        where table_schema = %s
          and table_name = 'precios'
          and column_name = 'precio_final'
    """, (NOMBRE_BD,))

    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            alter table precios
            add column precio_final decimal(10,2)
            generated always as (
                round(precio - (precio * descuento / 100), 2)
            ) stored after descuento
        """)
        conexion.commit()
    cursor.close()


def asegurarFechaAnterior(conexion):
    """Agrega al historial una fecha anterior fija de julio de 2020."""
    cursor = conexion.cursor()
    cursor.execute("""
        select count(*)
        from information_schema.columns
        where table_schema = %s
          and table_name = 'historial_precios'
          and column_name = 'fecha_anterior'
    """, (NOMBRE_BD,))

    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            alter table historial_precios
            add column fecha_anterior date
            not null default '2020-07-15' after precio_anterior
        """)
        conexion.commit()
    cursor.close()


# ---------------- VALIDACIONES CON REGEX ----------------
def validarTexto(texto):
    """Solo letras, acentos y espacios (nombres, generos, desarrolladores)."""
    patron = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$'
    return re.match(patron, texto) is not None

def validarPrecio(precio):
    """Numero positivo con hasta 2 decimales. Ej: 19.99 o 599"""
    patron = r'^\d+(\.\d{1,2})?$'
    return re.match(patron, precio) is not None

def validarAnio(anio):
    """4 digitos, entre 1970 y 2030."""
    patron = r'^(19[7-9]\d|20[0-2]\d|2030)$'
    return re.match(patron, anio) is not None

def validarURL(url):
    """Debe iniciar con http:// o https://"""
    patron = r'^https?://\S+$'
    return re.match(patron, url) is not None


# ---------------- GENERACION DE REPORTE (TXT) ----------------
def generarReporteTxt(datos, nombreArchivo="reporte_precios.txt"):
    """
    Recibe una lista de tuplas (juego, plataforma, precio) y genera
    un archivo de texto con la comparativa y estadisticas basicas.
    """
    try:
        totalAcumulado = 0        # acumulador
        contadorRegistros = 0      # contador
        with open(nombreArchivo, "w", encoding="utf-8") as archivo:
            archivo.write("=" * 70 + "\n")
            archivo.write(f"REPORTE DE PRECIOS - GENERADO: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
            archivo.write("=" * 70 + "\n\n")
            for fila in datos:
                archivo.write(f"Juego: {fila[0]:<30} Plataforma: {fila[1]:<12} Precio: ${fila[2]:.2f}\n")
                totalAcumulado += float(fila[2])       # expresion algoritmica (acumulador)
                contadorRegistros += 1                 # expresion algoritmica (contador)
            archivo.write("\n" + "-" * 70 + "\n")
            if contadorRegistros > 0:
                promedio = totalAcumulado / contadorRegistros   # jerarquia de operadores
                archivo.write(f"Total de registros: {contadorRegistros}\n")
                archivo.write(f"Precio promedio: ${promedio:.2f}\n")
            else:
                archivo.write("No habia precios registrados al momento de generar el reporte.\n")
        return True
    except Exception:
        return False
