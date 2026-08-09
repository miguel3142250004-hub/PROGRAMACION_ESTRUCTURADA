def insertar(datosJuego, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "insert into juegos (nombre, genero, desarrollador, anio_lanzamiento) values (%s,%s,%s,%s)",
                (datosJuego["nombre"], datosJuego["genero"], datosJuego["desarrollador"], datosJuego["anio"])
            )
            conexionBD.commit()
            return True
        else:
            return False
    except Exception:
        return False


def consultar(conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("select * from juegos order by nombre")
            return cursor.fetchall()
        else:
            return []
    except Exception:
        return []


def buscar(nombre, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("select * from juegos where nombre like %s", (f"%{nombre}%",))
            return cursor.fetchall()
        else:
            return []
    except Exception:
        return []


def actualizar(idJuego, datosJuego, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "update juegos set nombre=%s, genero=%s, desarrollador=%s, anio_lanzamiento=%s where id_juego=%s",
                (datosJuego["nombre"], datosJuego["genero"], datosJuego["desarrollador"], datosJuego["anio"], idJuego)
            )
            conexionBD.commit()
            return cursor.rowcount > 0
        else:
            return False
    except Exception:
        return False


def eliminar(idJuego, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("delete from juegos where id_juego=%s", (idJuego,))
            conexionBD.commit()
            return cursor.rowcount > 0
        else:
            return False
    except Exception:
        return False


def vaciar(conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("set foreign_key_checks=0")
            cursor.execute("truncate juegos")
            cursor.execute("set foreign_key_checks=1")
            conexionBD.commit()
            return True
        else:
            return False
    except Exception:
        return False
