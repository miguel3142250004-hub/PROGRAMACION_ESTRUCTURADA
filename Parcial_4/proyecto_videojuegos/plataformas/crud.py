def insertar(datosPlataforma, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "insert into plataformas (nombre, url_tienda) values (%s,%s)",
                (datosPlataforma["nombre"], datosPlataforma["url"])
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
            cursor.execute("select * from plataformas order by nombre")
            return cursor.fetchall()
        else:
            return []
    except Exception:
        return []


def buscar(nombre, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("select * from plataformas where nombre like %s", (f"%{nombre}%",))
            return cursor.fetchall()
        else:
            return []
    except Exception:
        return []


def actualizar(idPlataforma, datosPlataforma, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "update plataformas set nombre=%s, url_tienda=%s where id_plataforma=%s",
                (datosPlataforma["nombre"], datosPlataforma["url"], idPlataforma)
            )
            conexionBD.commit()
            return cursor.rowcount > 0
        else:
            return False
    except Exception:
        return False


def eliminar(idPlataforma, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("delete from plataformas where id_plataforma=%s", (idPlataforma,))
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
            cursor.execute("truncate plataformas")
            cursor.execute("set foreign_key_checks=1")
            conexionBD.commit()
            return True
        else:
            return False
    except Exception:
        return False
