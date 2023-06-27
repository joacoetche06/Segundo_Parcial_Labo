import sqlite3
from datos_jugadores import *
bandera_tabla = False
def crear_base_de_datos(nombre, puntuacion):
    global bandera_tabla
    with sqlite3.connect("mi_base_de_datos.db") as conexion:
        try:
            nombre_jugador = nombre
            puntuacion_jugador = puntuacion
            #Insertar datos

            insertar_datos(conexion, nombre_jugador, puntuacion_jugador)
            
            cursor = seleccionar_datos(conexion)

            lista_top = []
            for fila in cursor:
                lista_top.append({"Jugador": fila[1], "Score": fila[2]})
            return lista_top
        except:
            print("Error")



def crear_tabla(conexion):
    retorno = False
    sentencia = '''
                        create table Tabla_Puntaje
                        (
                            id integer primary key autoincrement,
                            nombre text,
                            puntuacion integer
                        )
                        
                        '''
    conexion.execute(sentencia)
    retorno = True
    return retorno

def insertar_datos(conexion, nombre_jugador, puntuacion_jugador):
    sentencia = '''
                insert into Tabla_Puntaje(nombre, puntuacion) values(?, ?)
                '''
    conexion.execute(sentencia, (nombre_jugador, puntuacion_jugador))

    

def seleccionar_datos(conexion):
    sentencia = 'select * from Tabla_Puntaje order by puntuacion desc limit 3'
    cursor = conexion.execute(sentencia)
    return cursor

