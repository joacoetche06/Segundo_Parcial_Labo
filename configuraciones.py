import pygame

def girar_imagenes(lista_original, flip_x: bool, flip_y: bool)-> list:
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada

def reescalar_imagen(lista_animaciones, W, H):
    for lista in lista_animaciones:
        for i in range(len(lista)):
            imagen = lista[i]
            lista[i] = pygame.transform.scale(imagen, (W,H))
            lista[i].convert()


piso_nivel_uno = pygame.image.load("Recursos/terreno/0.png")
piso_nivel_uno = pygame.transform.scale(piso_nivel_uno,(50,50))
piso_nivel_dos = pygame.image.load("Recursos/terreno/platform.png")
piso_nivel_dos = pygame.transform.scale(piso_nivel_dos,(50,50))
piso_nivel_tres = pygame.image.load("Recursos/items/piso_3.png")
piso_nivel_tres = pygame.transform.scale(piso_nivel_tres,(50,50))

pared_nivel_uno = pygame.image.load("Recursos/terreno/1.png")

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
    pygame.image.load("Recursos/fotos/salta2/11.png"),
    pygame.image.load("Recursos/fotos/salta2/11.png"),
    pygame.image.load("Recursos/fotos/salta2/11.png"),
    pygame.image.load("Recursos/fotos/salta2/11.png"),
    pygame.image.load("Recursos/fotos/salta2/11.png"),
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
    pygame.image.load("Recursos/fotos/ataca/5.png"),
    pygame.image.load("Recursos/fotos/ataca/5.png"),
    pygame.image.load("Recursos/fotos/ataca/5.png"),
    pygame.image.load("Recursos/fotos/ataca/5.png"),
    pygame.image.load("Recursos/fotos/ataca/5.png"),
    pygame.image.load("Recursos/fotos/ataca/5.png"),
    pygame.image.load("Recursos/fotos/ataca/5.png")    
]

fenix_volando = [
    pygame.image.load("Recursos/fenix/0.png"),
    pygame.image.load("Recursos/fenix/0.png"),
    pygame.image.load("Recursos/fenix/1.png"),
    pygame.image.load("Recursos/fenix/1.png"),
    pygame.image.load("Recursos/fenix/3.png"),
    pygame.image.load("Recursos/fenix/3.png"),
    pygame.image.load("Recursos/fenix/4.png"),
    pygame.image.load("Recursos/fenix/4.png"),
    pygame.image.load("Recursos/fenix/5.png"),
    pygame.image.load("Recursos/fenix/5.png"),
    pygame.image.load("Recursos/fenix/7.png"),
    pygame.image.load("Recursos/fenix/7.png")
    # pygame.image.load("Recursos/fenix/2.png"),
    # pygame.image.load("Recursos/fenix/0.png"),
    # pygame.image.load("Recursos/fenix/0.png"),
    # pygame.image.load("Recursos/fenix/0.png"),
    # pygame.image.load("Recursos/fenix/1.png"),
    # pygame.image.load("Recursos/fenix/1.png"),
    # pygame.image.load("Recursos/fenix/1.png"),
    # # pygame.image.load("Recursos/fenix/2.png"),
    # # pygame.image.load("Recursos/fenix/2.png"),
    # # pygame.image.load("Recursos/fenix/2.png"),
    # pygame.image.load("Recursos/fenix/3.png"),
    # pygame.image.load("Recursos/fenix/3.png"),
    # pygame.image.load("Recursos/fenix/3.png"),
    # pygame.image.load("Recursos/fenix/4.png"),
    # pygame.image.load("Recursos/fenix/4.png"),
    # pygame.image.load("Recursos/fenix/4.png"),
    # pygame.image.load("Recursos/fenix/5.png"),
    # pygame.image.load("Recursos/fenix/5.png"),
    # pygame.image.load("Recursos/fenix/5.png"),
    # # pygame.image.load("Recursos/fenix/6.png"),
    # # pygame.image.load("Recursos/fenix/6.png"),
    # # pygame.image.load("Recursos/fenix/6.png"),
    # pygame.image.load("Recursos/fenix/7.png"),
    # pygame.image.load("Recursos/fenix/7.png"),
    # pygame.image.load("Recursos/fenix/7.png")
    ]

fenix_volando_izquierda = girar_imagenes(fenix_volando, True, False)

hechizo_harry = [
    pygame.image.load("Recursos/hechizos/0.png"),
    pygame.image.load("Recursos/hechizos/1.png"),
    pygame.image.load("Recursos/hechizos/2.png")
]

hechizo_harry_izquierda = girar_imagenes(hechizo_harry, True, False)

araña_derecha = [
    pygame.image.load("Recursos/araña/movimiento/0.png"),
    pygame.image.load("Recursos/araña/movimiento/1.png"),
    pygame.image.load("Recursos/araña/movimiento/2.png"),
    pygame.image.load("Recursos/araña/movimiento/3.png")

]

araña_izquierda = girar_imagenes(araña_derecha, True, False)

araña_herida = araña_derecha = [
    pygame.image.load("Recursos/araña/herida/0.png"),
    pygame.image.load("Recursos/araña/herida/1.png"),
    pygame.image.load("Recursos/araña/herida/2.png"),
    pygame.image.load("Recursos/araña/herida/3.png")

]

duende_quieto = [
    pygame.image.load("Recursos/duende/quieto/0.png"),
    pygame.image.load("Recursos/duende/quieto/1.png"),
    pygame.image.load("Recursos/duende/quieto/2.png"),
    pygame.image.load("Recursos/duende/quieto/3.png"),
    pygame.image.load("Recursos/duende/quieto/4.png"),
    pygame.image.load("Recursos/duende/quieto/5.png")
]

duende_volando_izquierda = [
    pygame.image.load("Recursos/duende/volar/0.png"),
    pygame.image.load("Recursos/duende/volar/0.png"),
    pygame.image.load("Recursos/duende/volar/0.png"),
    pygame.image.load("Recursos/duende/volar/1.png"),
    pygame.image.load("Recursos/duende/volar/1.png"),
    pygame.image.load("Recursos/duende/volar/1.png")
]

duende_volando = girar_imagenes(duende_volando_izquierda, True, False)

duende_herido = [
    pygame.image.load("Recursos/duende/herido/0.png"),
    pygame.image.load("Recursos/duende/herido/1.png"),
    pygame.image.load("Recursos/duende/herido/2.png"),
    pygame.image.load("Recursos/duende/herido/3.png")
]

duende_atacando = [
    pygame.image.load("Recursos/duende/atacar/0.png"),
    pygame.image.load("Recursos/duende/atacar/1.png"),
    pygame.image.load("Recursos/duende/atacar/2.png"),
    pygame.image.load("Recursos/duende/atacar/3.png"),
    pygame.image.load("Recursos/duende/atacar/4.png"),
    pygame.image.load("Recursos/duende/atacar/5.png")
]

barra_vida = [
    pygame.image.load("Recursos/vida/0.png"),
    pygame.image.load("Recursos/vida/1.png"),
    pygame.image.load("Recursos/vida/2.png"),
    pygame.image.load("Recursos/vida/3.png"),
    pygame.image.load("Recursos/vida/4.png"),
    pygame.image.load("Recursos/vida/5.png")
]

serpiente_derecha = [
    pygame.image.load("Recursos/serpiente/movimiento/0.png"),
    pygame.image.load("Recursos/serpiente/movimiento/1.png"),
    pygame.image.load("Recursos/serpiente/movimiento/2.png"),
    pygame.image.load("Recursos/serpiente/movimiento/3.png"),
    pygame.image.load("Recursos/serpiente/movimiento/4.png")
]

serpiente_izquierda = girar_imagenes(serpiente_derecha, True, False)

serpiente_herida = [
    pygame.image.load("Recursos/serpiente/herida/0.png"),
    pygame.image.load("Recursos/serpiente/herida/1.png"),
    pygame.image.load("Recursos/serpiente/herida/2.png"),
    pygame.image.load("Recursos/serpiente/herida/3.png")
                    ]

voldemort_quieto = [
    pygame.image.load("Recursos/voldemort/quieto/0.png"),
    pygame.image.load("Recursos/voldemort/quieto/0.png"),
    pygame.image.load("Recursos/voldemort/quieto/0.png"),
    pygame.image.load("Recursos/voldemort/quieto/0.png"),
    pygame.image.load("Recursos/voldemort/quieto/0.png"),
    pygame.image.load("Recursos/voldemort/quieto/0.png"),
    pygame.image.load("Recursos/voldemort/quieto/0.png"),
    pygame.image.load("Recursos/voldemort/quieto/0.png"),
    pygame.image.load("Recursos/voldemort/quieto/1.png"),
    pygame.image.load("Recursos/voldemort/quieto/1.png"),
    pygame.image.load("Recursos/voldemort/quieto/1.png"),
    pygame.image.load("Recursos/voldemort/quieto/1.png"),
    pygame.image.load("Recursos/voldemort/quieto/1.png"),
    pygame.image.load("Recursos/voldemort/quieto/1.png"),
    pygame.image.load("Recursos/voldemort/quieto/1.png"),
    pygame.image.load("Recursos/voldemort/quieto/1.png")
    ]

voldemort_derecha = [
    pygame.image.load("Recursos/voldemort/ataca/4.png"),
    pygame.image.load("Recursos/voldemort/ataca/4.png"),
    pygame.image.load("Recursos/voldemort/ataca/4.png"),
    pygame.image.load("Recursos/voldemort/ataca/4.png"),
    pygame.image.load("Recursos/voldemort/ataca/4.png"),
    pygame.image.load("Recursos/voldemort/ataca/4.png"),
    pygame.image.load("Recursos/voldemort/ataca/4.png"),
    pygame.image.load("Recursos/voldemort/ataca/4.png"),
    pygame.image.load("Recursos/voldemort/ataca/5.png"),
    pygame.image.load("Recursos/voldemort/ataca/5.png"),
    pygame.image.load("Recursos/voldemort/ataca/5.png"),
    pygame.image.load("Recursos/voldemort/ataca/5.png"),
    pygame.image.load("Recursos/voldemort/ataca/5.png"),
    pygame.image.load("Recursos/voldemort/ataca/5.png"),
    pygame.image.load("Recursos/voldemort/ataca/5.png"),
    pygame.image.load("Recursos/voldemort/ataca/5.png")
]

voldemort_izquierda = girar_imagenes(voldemort_derecha, True, False)

voldemort_caido = [
    pygame.image.load("Recursos/voldemort/caido/0.png"),
    pygame.image.load("Recursos/voldemort/caido/1.png"),
    pygame.image.load("Recursos/voldemort/caido/2.png")
]

hechizo_voldemort = [
    pygame.image.load("Recursos/hechizos/6.png"),
    pygame.image.load("Recursos/hechizos/7.png")
]

piedra =  pygame.image.load("Recursos/items/piedra.png")
piedra = pygame.transform.scale(piedra, (30,28))

cabeza_vida_voldemort = pygame.image.load("Recursos/voldemort/vida.png")
cabeza_vida_voldemort = pygame.transform.scale(cabeza_vida_voldemort, (60,60))