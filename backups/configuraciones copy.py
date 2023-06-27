import pygame

def girar_imagenes(lista_original, flip_x: bool, flip_y: bool)-> list:
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada

def reescalar_imagen(lista_animaciones, bandera, W, H):
    for lista in lista_animaciones:
        for i in range(len(lista)):
            imagen = lista[i]
            if bandera == True:#si quiero que lo reescale a harry
                lista[i] = pygame.transform.scale2x(imagen)#, (W,H))
            else:
                lista[i] = pygame.transform.scale(imagen, (W,H))


personaje_quieto = [
    pygame.image.load("Recursos/fotos/quieto/2.png"),
    pygame.image.load("Recursos/fotos/quieto/2.png"),
    pygame.image.load("Recursos/fotos/quieto/2.png"),
    pygame.image.load("Recursos/fotos/quieto/2.png"),
    pygame.image.load("Recursos/fotos/quieto/2.png"),
    pygame.image.load("Recursos/fotos/quieto/2.png"),
    pygame.image.load("Recursos/fotos/quieto/2.png"),
    pygame.image.load("Recursos/fotos/quieto/3.png"),
    pygame.image.load("Recursos/fotos/quieto/3.png"),
    pygame.image.load("Recursos/fotos/quieto/3.png"),
    pygame.image.load("Recursos/fotos/quieto/3.png"),
    pygame.image.load("Recursos/fotos/quieto/3.png"),
    pygame.image.load("Recursos/fotos/quieto/3.png"),
    pygame.image.load("Recursos/fotos/quieto/3.png"),
    pygame.image.load("Recursos/fotos/quieto/3.png"),
    pygame.image.load("Recursos/fotos/quieto/3.png"),
    pygame.image.load("Recursos/fotos/quieto/3.png"),
    pygame.image.load("Recursos/fotos/quieto/3.png"),
    pygame.image.load("Recursos/fotos/quieto/3.png")

]


personaje_camina = [    
    pygame.image.load("Recursos/fotos/camina/2.png"),
    pygame.image.load("Recursos/fotos/camina/8.png")
]


personaje_salta = [    
    pygame.image.load("Recursos/fotos/salta2/6.png"),
    pygame.image.load("Recursos/fotos/salta2/7.png"),
    pygame.image.load("Recursos/fotos/salta2/8.png"),
    pygame.image.load("Recursos/fotos/salta2/9.png"),
    pygame.image.load("Recursos/fotos/salta2/10.png"),
    pygame.image.load("Recursos/fotos/salta2/11.png"),
]

personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)

personaje_ataca = [
    pygame.image.load("Recursos/fotos/ataca/0.png"),
    pygame.image.load("Recursos/fotos/ataca/1.png"),
    pygame.image.load("Recursos/fotos/ataca/2.png"),
    pygame.image.load("Recursos/fotos/ataca/3.png"),
    pygame.image.load("Recursos/fotos/ataca/4.png"),
    pygame.image.load("Recursos/fotos/ataca/5.png"),
    pygame.image.load("Recursos/fotos/ataca/5.png"),
    pygame.image.load("Recursos/fotos/ataca/5.png")    
]

fenix_volando = [
    pygame.image.load("Recursos/fenix/0.png"),
    pygame.image.load("Recursos/fenix/0.png"),
    pygame.image.load("Recursos/fenix/0.png"),
    pygame.image.load("Recursos/fenix/1.png"),
    pygame.image.load("Recursos/fenix/1.png"),
    pygame.image.load("Recursos/fenix/1.png"),
    # pygame.image.load("Recursos/fenix/2.png"),
    # pygame.image.load("Recursos/fenix/2.png"),
    # pygame.image.load("Recursos/fenix/2.png"),
    pygame.image.load("Recursos/fenix/3.png"),
    pygame.image.load("Recursos/fenix/3.png"),
    pygame.image.load("Recursos/fenix/3.png"),
    pygame.image.load("Recursos/fenix/4.png"),
    pygame.image.load("Recursos/fenix/4.png"),
    pygame.image.load("Recursos/fenix/4.png"),
    pygame.image.load("Recursos/fenix/5.png"),
    pygame.image.load("Recursos/fenix/5.png"),
    pygame.image.load("Recursos/fenix/5.png"),
    # pygame.image.load("Recursos/fenix/6.png"),
    # pygame.image.load("Recursos/fenix/6.png"),
    # pygame.image.load("Recursos/fenix/6.png"),
    pygame.image.load("Recursos/fenix/7.png"),
    pygame.image.load("Recursos/fenix/7.png"),
    pygame.image.load("Recursos/fenix/7.png")
    ]

fenix_volando_izquierda = girar_imagenes(fenix_volando, True, False)

hechizo_harry = [
    pygame.image.load("Recursos/hechizos/0.png"),
    pygame.image.load("Recursos/hechizos/1.png"),
    pygame.image.load("Recursos/hechizos/2.png")
]

hechizo_harry_izquierda = girar_imagenes(hechizo_harry, True, False)
# personaje_quieto = [
#     pygame.image.load("Recursos/fotos2/quieto/0.png"),
#     pygame.image.load("Recursos/fotos2/quieto/1.png"),
#     pygame.image.load("Recursos/fotos2/quieto/2.png"),
#     pygame.image.load("Recursos/fotos2/quieto/3.png"),
#     pygame.image.load("Recursos/fotos2/quieto/4.png")
# ]

# personaje_camina = [
#     pygame.image.load("Recursos/fotos2/camina/0.png"),
#     pygame.image.load("Recursos/fotos2/camina/1.png"),
#     pygame.image.load("Recursos/fotos2/camina/2.png"),
#     pygame.image.load("Recursos/fotos2/camina/3.png"),
#     pygame.image.load("Recursos/fotos2/camina/4.png"),
#     pygame.image.load("Recursos/fotos2/camina/5.png"),
#     pygame.image.load("Recursos/fotos2/camina/6.png"),
#     pygame.image.load("Recursos/fotos2/camina/7.png"),
#     pygame.image.load("Recursos/fotos2/camina/8.png")
# ]

# personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)


# personaje_salta = [
#     pygame.image.load("Recursos/fotos2/salta/0.png"),
#     pygame.image.load("Recursos/fotos2/salta/1.png"),
#     pygame.image.load("Recursos/fotos2/salta/2.png"),
#     pygame.image.load("Recursos/fotos2/salta/3.png"),
#     pygame.image.load("Recursos/fotos2/salta/4.png")
# ]
#####################################################################################

# personaje_quieto = [
#     pygame.image.load("Recursos/fotos/quieto/0.png"),
#     pygame.image.load("Recursos/fotos/quieto/1.png"),
#     pygame.image.load("Recursos/fotos/quieto/a.png"),
#     #pygame.image.load("Recursos/fotos/quieto/3.png"),
#     pygame.image.load("Recursos/fotos/quieto/2.png"),
#     pygame.image.load("Recursos/fotos/quieto/4.png")
#     # pygame.image.load("Recursos/fotos/quieto/5.png")

# ]