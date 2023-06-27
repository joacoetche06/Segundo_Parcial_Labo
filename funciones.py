import pygame


def dibujar_estructuras(ancho_pantalla, imagen):
    
    ancho_piso = imagen.get_width()
    cantidad_repeticiones = int(ancho_pantalla / ancho_piso)
    ancho_piso_total = imagen.get_width() * cantidad_repeticiones
    alto_piso = imagen.get_height()

    superficie_piso = pygame.Surface((ancho_piso_total, alto_piso)).convert()

    for i in range(cantidad_repeticiones):
        superficie_piso.blit(imagen, (i * ancho_piso, 0))

    return superficie_piso

def dibujar_cuadrados(pantalla, lados, color):
    if lados != None:
        for lado in lados:
            pygame.draw.rect(pantalla, color, lados[lado], 2)

# def verificar_colision_desaparicion_item(personaje_lado, item, sonido):
#     if personaje_lado.colliderect(item.rectangulo):
#         item.rectangulo = None
#         item.lados = None
#         if sonido != None:
#             sonido.play()

#     return item.rectangulo


# def mover_hechizo(que_hace, atacando, hechizo, pantalla, velocidad_hechizo):
#     if (que_hace == "Ataca" or atacando == True) and hechizo.lados != None:
#         animar_imagen(pantalla, hechizo.rectangulo, hechizo_harry)
#         mover_imagen(hechizo.lados, velocidad_hechizo)

# def verificar_colision_hechizo(hechizo, plataforma_uno, plataforma_dos, W, atacando, duende):
#     if hechizo.rectangulo != None:
#         # if hechizo.rectangulo.colliderect(duende.rectangulo):
#         #     print(hechizo.rectangulo)
#         if duende.rectangulo != None:
#             duende.rectangulo = verificar_colision_desaparicion_item(hechizo.rectangulo, duende, None)

#         if (hechizo.rectangulo.colliderect(plataforma_uno.rectangulo)
#         or hechizo.rectangulo.colliderect(plataforma_dos.rectangulo)
#         or hechizo.rectangulo.x > W) or duende.rectangulo == None:
#             atacando = False
#             hechizo.rectangulo = None
#             hechizo.lados = None
#     return atacando


# def temporizar(pantalla, fuente, temporizador_tick, temporizador_tiempo_anterior):
#     global tiempo_restante
    
#     tiempo_actual = pygame.time.get_ticks()
#     tiempo_transcurrido = tiempo_actual - temporizador_tiempo_anterior
#     if tiempo_transcurrido >= temporizador_tick:
#         tiempo_restante -= 1
#         print(tiempo_restante)
#         if tiempo_restante <= 0:
#             # El temporizador ha terminado, puedes agregar aquí la lógica que deseas realizar cuando el tiempo se acaba
#             tiempo_restante = 0
#         temporizador_tiempo_anterior = tiempo_actual

#     minutos = tiempo_restante // 60
#     segundos = tiempo_restante % 60
#     temporizador = fuente.render(f"{minutos:02}:{segundos:02}", True, (255, 0, 0), "White")

#     pantalla.blit(temporizador, (1187,1))