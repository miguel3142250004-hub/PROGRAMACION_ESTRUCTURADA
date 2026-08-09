def insertar(datosPrecio, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "insert into precios (id_juego, id_plataforma, precio, moneda, descuento) values (%s,%s,%s,%s,%s)",
                (datosPrecio["id_juego"], datosPrecio["id_plataforma"], datosPrecio["precio"],
                 datosPrecio["moneda"], datosPrecio["descuento"])
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
            cursor.execute("""
                select p.id_precio, j.nombre, pl.nombre, p.precio, p.moneda,
                       p.descuento, p.fecha_actualizacion, p.precio_final
                from precios p
                inner join juegos j on p.id_juego = j.id_juego
                inner join plataformas pl on p.id_plataforma = pl.id_plataforma
                order by j.nombre
            """)
            return cursor.fetchall()
        else:
            return []
    except Exception:
        return []


def buscarPorJuego(nombreJuego, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("""
                select p.id_precio, j.nombre, pl.nombre, p.precio, p.moneda,
                       p.descuento, p.fecha_actualizacion, p.precio_final
                from precios p
                inner join juegos j on p.id_juego = j.id_juego
                inner join plataformas pl on p.id_plataforma = pl.id_plataforma
                where j.nombre like %s
                order by p.precio_final asc
            """, (f"%{nombreJuego}%",))
            return cursor.fetchall()
        else:
            return []
    except Exception:
        return []


def obtenerPrecioActual(idPrecio, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("select precio from precios where id_precio=%s", (idPrecio,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado != None else None
        else:
            return None
    except Exception:
        return None


def actualizar(idPrecio, nuevoPrecio, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "update precios set precio=%s, fecha_actualizacion=now() where id_precio=%s",
                (nuevoPrecio, idPrecio)
            )
            conexionBD.commit()
            return cursor.rowcount > 0
        else:
            return False
    except Exception:
        return False


def eliminar(idPrecio, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("delete from precios where id_precio=%s", (idPrecio,))
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
            cursor.execute("truncate precios")
            cursor.execute("set foreign_key_checks=1")
            conexionBD.commit()
            return True
        else:
            return False
    except Exception:
        return False


def listarJuegosPlataformas(conexionBD):
    """Trae los catalogos de juegos y plataformas para mostrarlos como apoyo al capturar un precio."""
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("select id_juego, nombre from juegos order by nombre")
            juegosBD = cursor.fetchall()
            cursor.execute("select id_plataforma, nombre from plataformas order by nombre")
            plataformasBD = cursor.fetchall()
            return juegosBD, plataformasBD
        else:
            return [], []
    except Exception:
        return [], []
