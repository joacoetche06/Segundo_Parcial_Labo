import pygame, sys, time

from configuraciones import *
from modo import *
from movimiento import *
from funciones import *

from Clase_Personaje import *
from Clase_Plataforma import *
from Clase_Proyectiles import *


W, H = 1300, 700
FPS = 18

pygame.init()
RELOJ = pygame.time.Clock()

PANTALLA = pygame.display.set_mode((W,H))

#ICONO
icono = pygame.image.load("Recursos/fotos/logo.png")
pygame.display.set_icon(icono)

#FONDO
fondo = pygame.image.load("Recursos/fotos/fondo_1.png")
fondo = pygame.transform.scale(fondo, (W,H))

#PERSONAJE

x_inicial = H/2 - 200
y_inicial = 450
# contador_pasos = 0
velocidad = 30

#posicion_actual_x = 0

lista_animaciones = [personaje_quieto, personaje_camina, personaje_camina_izquierda, personaje_salta,
                    personaje_ataca]


reescalar_imagen(lista_animaciones, True, 60, 100)


# rectangulo_personaje = personaje_camina[0].get_rect()
# rectangulo_personaje.x = x_inicial
# rectangulo_personaje.y = y_inicial

harry = Personaje(personaje_camina[0], x_inicial, y_inicial, "Recursos/sonidos/ascendio_2.mp3")


# lados_personaje = obtener_rectangulos(personaje.rectangulo)


# que_hace = "Quieto"

#SALTO
gravedad = 1
potencia_salto = -15
limite_velocidad_caida = 10
# esta_saltando = False
# desplazamiento_y = 0

#SUPERFICIE

piso = pygame.Rect(0,0,W,20)
piso.top = harry.rectangulo.bottom

#PLATAFORMA
# plataforma = pygame.image.load("Recursos/items/plataforma.png")
# plataforma = pygame.transform.scale(plataforma, (100, 100))
# rectangulo_plataforma = plataforma.get_rect()
# rectangulo_plataforma. x = 400
# rectangulo_plataforma. y = 450

# plataforma_dos = pygame.image.load("Recursos/items/plataforma.png")
# plataforma_dos = pygame.transform.scale(plataforma_dos, (100, 100))
# rectangulo_plataforma_dos = plataforma_dos.get_rect()
# rectangulo_plataforma_dos. x = 600
# rectangulo_plataforma_dos. y = 350

plataforma_uno = Plataformas("Recursos/items/plataforma.png", (100,100), 400, 450)
plataforma_dos = Plataformas("Recursos/items/plataforma.png", (100,100), 600, 350)


lados_piso= obtener_rectangulos(piso)

# lados_plataforma = obtener_rectangulos(rectangulo_plataforma)

# lados_plataforma_dos = obtener_rectangulos(rectangulo_plataforma_dos)

#LISTA PLATAFORMAS
lista_plataformas = [lados_piso, plataforma_uno.lados, plataforma_dos.lados]

#FENIX
x_inicial_fenix = 100
y_inicial_fenix = 100
# contador_pasos = 0
velocidad_fenix = 25

lista_animaciones_fenix = [fenix_volando, fenix_volando_izquierda]

reescalar_imagen(lista_animaciones_fenix, False, 60, 100)

fenix = Personaje(fenix_volando[4], x_inicial_fenix, y_inicial_fenix, "Recursos/sonidos/fenix.mp3")

# lados_fenix = obtener_rectangulos(fenix.rectangulo)

# #HECHIZO
#(210, 488)
x_inicial_hechizo = harry.lados['right'].x + 25
y_inicial_hechizo = harry.rectangulo.y + 30
velocidad_hechizo = 10

lista_imagenes_hechizo = [hechizo_harry, hechizo_harry_izquierda]
reescalar_imagen(lista_imagenes_hechizo, False, 30, 30)


hechizo = Hechizo(x_inicial_hechizo, y_inicial_hechizo, hechizo_harry[0], "Recursos/sonidos/expelliarmus_2.ogg")

bandera = True
tiempo = 0

contador_hechizo = 0

atacando = False

presionada= True


while True:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and harry.rectangulo.x < W - velocidad - harry.rectangulo.width:
        que_hace = "Derecha"
    elif keys[pygame.K_LEFT] and harry.rectangulo.x > 25:
        que_hace = "Izquierda"
    elif keys[pygame.K_UP] and presionada == True:                
        que_hace = "Salta"
        harry.sonido.play()
        presionada = False
    elif keys[pygame.K_SPACE] and presionada == True:
        que_hace = "Ataca"
        tiempo = time.time()
        atacando = True
        hechizo.sonido.play()
        presionada = False
    elif time.time() - 0.2 > tiempo:
        que_hace = "Quieto"
        presionada = True

    
        

    PANTALLA.blit(fondo, (0,0))
    actualizar_pantalla(PANTALLA, fondo, que_hace, velocidad, harry.lados, plataforma_uno,
                        plataforma_dos, lista_plataformas, potencia_salto,
                        gravedad, limite_velocidad_caida, fenix, W, velocidad_fenix)#,
                        #hechizo, velocidad_hechizo)

    # if que_hace == "Ataca" or atacando == True:
    #     animar_imagen(PANTALLA, hechizo.rectangulo, hechizo_harry)
    #     mover_imagen(hechizo.lados, velocidad_hechizo)

    # if hechizo.rectangulo.colliderect(plataforma_uno.rectangulo) or hechizo.rectangulo.x > W:
    #     atacando = False
    #     hechizo.rectangulo.x = harry.lados['right'].x + 25

    # for imagen in lista_imagenes_hechizo:
    #     largo = len(lista_imagenes_hechizo)
    #     if contador_hechizo >= largo:
    #         contador_hechizo = 0
    #     lista_imagenes_hechizo[contador_hechizo]
    #     hechizo.rectangulo.x += velocidad_hechizo
    #     PANTALLA.blit(hechizo_harry[contador_hechizo], rectangulo_hechizo)
    #     contador_hechizo += 1
        
        # if hechizo.rectangulo.x < W - velocidad_hechizo - hechizo.rectangulo.width:
        #     hechizo.rectangulo = None



    # if fenix.rectangulo != None:
        # fenix.rectangulo = verificar_colision_desaparicion(harry.lados["top"], fenix.rectangulo, fenix.sonido)
    
    
    
    # if harry.lados["top"].colliderect(fenix.rectangulo):
    #     fenix.rectangulo.y = -100

    

    # print(pygame.mouse.get_pos())
    

    if get_mode():

        for lado in lados_piso:
            pygame.draw.rect(PANTALLA, "Green", lados_piso[lado], 2)
        for lado in harry.lados:
            pygame.draw.rect(PANTALLA, "Black", harry.lados[lado], 2)
        for lado in plataforma_uno.lados:
            pygame.draw.rect(PANTALLA, "White", plataforma_uno.lados[lado], 2)
        for lado in plataforma_dos.lados:
            pygame.draw.rect(PANTALLA, "White", plataforma_dos.lados[lado], 2)
        for lado in fenix.lados:
            pygame.draw.rect(PANTALLA, "White", fenix.lados[lado], 2)
        for lado in hechizo.lados:
            pygame.draw.rect(PANTALLA, "Brown", hechizo.lados[lado], 2)


    pygame.display.flip()