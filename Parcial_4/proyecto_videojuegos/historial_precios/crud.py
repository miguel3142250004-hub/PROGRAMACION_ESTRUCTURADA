def insertar(idPrecio, precioAnterior, precioNuevo, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "insert into historial_precios (id_precio, precio_anterior, precio_nuevo) values (%s,%s,%s)",
                (idPrecio, precioAnterior, precioNuevo)
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
                select h.id_historial, j.nombre, pl.nombre, h.precio_anterior,
                       h.precio_nuevo, h.fecha_cambio, h.fecha_anterior
                from historial_precios h
                inner join precios p on h.id_precio = p.id_precio
                inner join juegos j on p.id_juego = j.id_juego
                inner join plataformas pl on p.id_plataforma = pl.id_plataforma
                order by h.fecha_cambio desc
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
                select h.id_historial, j.nombre, pl.nombre, h.precio_anterior,
                       h.precio_nuevo, h.fecha_cambio, h.fecha_anterior
                from historial_precios h
                inner join precios p on h.id_precio = p.id_precio
                inner join juegos j on p.id_juego = j.id_juego
                inner join plataformas pl on p.id_plataforma = pl.id_plataforma
                where j.nombre like %s
                order by h.fecha_cambio desc
            """, (f"%{nombreJuego}%",))
            return cursor.fetchall()
        else:
            return []
    except Exception:
        return []


def actualizar(idHistorial, precioAnterior, precioNuevo, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "update historial_precios set precio_anterior=%s, precio_nuevo=%s where id_historial=%s",
                (precioAnterior, precioNuevo, idHistorial)
            )
            conexionBD.commit()
            return cursor.rowcount > 0
        else:
            return False
    except Exception:
        return False


def eliminar(idHistorial, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("delete from historial_precios where id_historial=%s", (idHistorial,))
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
            cursor.execute("truncate historial_precios")
            conexionBD.commit()
            return True
        else:
            return False
    except Exception:
        return False
