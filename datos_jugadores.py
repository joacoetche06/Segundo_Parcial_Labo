def pedir_datos():
    nombre_jugador = input("Escriba su nombre: ")
    puntuacion_jugador = int(input("Escriba su puntuación: "))

    diccionario = {"nombre": nombre_jugador,
                    "puntuacion": puntuacion_jugador
                    }
    
    return diccionario