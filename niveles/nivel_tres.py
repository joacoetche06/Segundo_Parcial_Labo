import pygame

from configuraciones import *
from modo import *
from funciones import dibujar_estructuras

from Clase_Personaje import Personaje
from Clase_Plataforma import Plataformas
from Clase_Enemigo import Enemigo
from Clase_Secundario import Secundario
from Clase_Boss import Voldemort
from Clase_Trampas import Trampa



from GUI_form_principal import *

from niveles.nivel import *

class NivelTres(Nivel):
    def __init__(self, pantalla: pygame.surface):
        #PANTALLA
        W = pantalla.get_width()
        H = pantalla.get_height()

        #ICONO
        icono = pygame.image.load("Recursos/fotos/logo.png")
        pygame.display.set_icon(icono)

        #FONDO
        fondo = pygame.image.load("Recursos/fotos/fondo3.jpg")
        fondo = pygame.transform.scale(fondo, (W,H))

        #PERSONAJE

        x_inicial = H/2 - 200
        y_inicial = W/2 - 160
        velocidad = 20


        lista_animaciones = [personaje_quieto, personaje_camina, personaje_camina_izquierda, personaje_salta,
                            personaje_ataca]

        reescalar_imagen(lista_animaciones, 42, 88)

        harry = Personaje(personaje_camina[0], x_inicial, y_inicial, "Recursos/sonidos/Ascendio1.wav", velocidad)

        #SUPERFICIE
        plataforma_uno = Plataformas("Recursos/items/plataforma_3.png", (90,32), 350, 375)
        plataforma_dos = Plataformas("Recursos/items/plataforma_3.png", (90,32), 625, 450)

        superficie_piso_principal = dibujar_estructuras(W, piso_nivel_tres)
        superficie_piso_uno = dibujar_estructuras(W - 800, piso_nivel_tres)
        superficie_piso_dos = dibujar_estructuras(W - 1000, piso_nivel_tres)
        superficie_piso_tres = dibujar_estructuras(W - 100, piso_nivel_tres)

        y_piso_principal = harry.rectangulo.bottom - 10
        piso_principal = Plataformas(superficie_piso_principal, (W,20), 0, y_piso_principal)
        x_piso_uno = 800
        y_piso_uno = 455
        x_piso_dos = 0
        y_piso_dos = 300
        x_piso_tres = 500
        y_piso_tres = 200
        piso_uno = Plataformas(superficie_piso_uno, (50,20), x_piso_uno, y_piso_uno + 30)
        piso_dos = Plataformas(superficie_piso_dos, (10,0), x_piso_dos, y_piso_dos + 30)
        piso_tres = Plataformas(superficie_piso_tres, (W - 200, 20), x_piso_tres, y_piso_tres + 30)

        #LISTA PLATAFORMAS
        lista_plataformas = [piso_principal, piso_uno, piso_dos, piso_tres, plataforma_uno, plataforma_dos]#, plataforma_tres]

        #TRAMPA
        lista_pinchos = []
        pincho_uno = Trampa("Recursos/items/spike.png", (48,21), 600, piso_tres.rectangulo.top - 21)
        pincho_dos = Trampa("Recursos/items/spike.png", (48,21), pincho_uno.rectangulo.x + 48, piso_tres.rectangulo.top - 21)
        pincho_tres = Trampa("Recursos/items/spike.png", (48,21), pincho_dos.rectangulo.x + 48, piso_tres.rectangulo.top - 21)

        lista_pinchos.append(pincho_uno)
        lista_pinchos.append(pincho_dos)
        lista_pinchos.append(pincho_tres)

        #PIEDRA
        x_inicial_piedra = piso_tres.rectangulo.x
        y_inicial_piedra = piso_tres.rectangulo.y - 30



        piedra_resurrecion = Secundario(x_inicial_piedra, y_inicial_piedra, piedra, None, 0)


        #HECHIZO

        lista_imagenes_hechizo = [hechizo_harry, hechizo_harry_izquierda]
        reescalar_imagen(lista_imagenes_hechizo, 30, 30)


        #SERPIENTES


        velocidad_araña = 10

        lista_animaciones_araña = [serpiente_derecha, serpiente_izquierda, serpiente_herida]

        reescalar_imagen(lista_animaciones_araña, 35, 30)

        serpiente_uno = Enemigo(x_piso_dos, y_piso_dos - 5, serpiente_derecha[0], "Recursos/sonidos/serpiente.mp3", velocidad_araña, serpiente_derecha, serpiente_izquierda, serpiente_herida)
        serpiente_dos = Enemigo(x_piso_uno + 50, y_piso_uno - 5, serpiente_derecha[0], "Recursos/sonidos/serpiente.mp3", velocidad_araña, serpiente_derecha, serpiente_izquierda, serpiente_herida)
        serpiente_tres = Enemigo(W-50, y_piso_principal - 30, serpiente_derecha[0], "Recursos/sonidos/serpiente.mp3", velocidad_araña, serpiente_derecha, serpiente_izquierda, serpiente_herida)


        lista_enemigos = []

        lista_enemigos.append(serpiente_uno)
        lista_enemigos.append(serpiente_dos)
        lista_enemigos.append(serpiente_tres)
        #BARRA DE VIDA
        for imagen in barra_vida:
            pygame.transform.scale(imagen, (100,60))


        pared_uno = Plataformas("Recursos/items/0.png", (20,84), piso_uno.rectangulo.x, piso_uno.rectangulo.y - 84)
        lista_plataformas.append(pared_uno)
        pared_dos = Plataformas("Recursos/items/0.png", (28,84), piso_dos.lados['right'].x - 25, piso_dos.rectangulo.y - 84)
        lista_plataformas.append(pared_dos)

        lista_animaciones_voldemort = [voldemort_izquierda, voldemort_quieto]

        reescalar_imagen(lista_animaciones_voldemort, 61, 110)

        voldemort = Voldemort(W - 100, piso_tres.rectangulo.y - 110, voldemort_quieto[0], "Recursos/sonidos/avadakadavra.OGG", 15)

        super().__init__(pantalla, harry, lista_plataformas, fondo, piedra_resurrecion, lista_enemigos, 60, lista_pinchos, "tres",voldemort)