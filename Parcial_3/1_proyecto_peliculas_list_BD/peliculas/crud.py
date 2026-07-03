import funciones

def insertar(peli,conexionBD):
    try:
        if conexionBD!=None:
          cursor=conexionBD.cursor()
          cursor.execute("insert into peliculas values (null,%s)",(peli,))
          conexionBD.commit()
          return True
        else:
          return False   
    except:
        return False 
    
def consultar(conexionBD):
    try:
       if conexionBD!=None:
           cursor=conexionBD.cursor()
           cursor.execute("select * from peliculas")
           return cursor.fetchall()
       else:
           return []
    except:
        return []  

def vaciar(conexionBD):
    try:
        if conexionBD!=None:
          cursor=conexionBD.cursor()
          cursor.execute("truncate peliculas")   
          conexionBD.commit()
          return True
        else:
          return False   
    except:
        return False         