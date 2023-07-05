import pygame

from configuraciones import *
from modo import *
from funciones import dibujar_estructuras

from Clase_Personaje import Personaje
from Clase_Plataforma import Plataformas
from Clase_Enemigo import Enemigo
from Clase_Secundario import Secundario
from Clase_Trampas import Trampa



from GUI_form_principal import *

from niveles.nivel import *

class NivelDos(Nivel):
    def __init__(self, pantalla: pygame.surface):
        #PANTALLA
        W = pantalla.get_width()
        H = pantalla.get_height()

        #ICONO
        icono = pygame.image.load("Recursos/fotos/logo.png")
        pygame.display.set_icon(icono)

        #FONDO
        fondo = pygame.image.load("Recursos/fotos/fondo_2.jpg")
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
        plataforma_uno = Plataformas("Recursos/items/MergedImages.png", (150,32), 350, 350)
        plataforma_dos = Plataformas("Recursos/items/MergedImages.png", (150,32), 650, 450)
        plataforma_tres = Plataformas("Recursos/items/MergedImages.png", (150,32), 600, 250)

        superficie_piso_principal = dibujar_estructuras(W, piso_nivel_dos)
        superficie_piso_uno = dibujar_estructuras(W - 900, piso_nivel_dos)
        superficie_piso_dos = dibujar_estructuras(W - 1000, piso_nivel_dos)
        superficie_piso_tres = dibujar_estructuras(W - 900, piso_nivel_dos)

        y_piso_principal = harry.rectangulo.bottom - 10
        piso_principal = Plataformas(superficie_piso_principal, (W,20), 0, y_piso_principal)
        x_piso_uno = 900
        y_piso_uno = 400
        x_piso_dos = 0
        y_piso_dos = 300
        x_piso_tres = 1000
        y_piso_tres = 200
        piso_uno = Plataformas(superficie_piso_uno, (50,20), x_piso_uno, y_piso_uno + 30)
        piso_dos = Plataformas(superficie_piso_dos, (10,0), x_piso_dos, y_piso_dos + 30)
        piso_tres = Plataformas(superficie_piso_tres, (W - plataforma_tres.rectangulo.x,20), x_piso_tres, y_piso_tres + 30)

        #LISTA PLATAFORMAS
        lista_plataformas = [piso_principal, piso_uno, piso_dos, piso_tres, plataforma_uno, plataforma_dos, plataforma_tres]


        #TRAMPA
        lista_pinchos = []
        pincho_uno = Trampa("Recursos/items/spike.png", (48,21), 400, piso_principal.rectangulo.top - 21)
        pincho_dos = Trampa("Recursos/items/spike.png", (48,21), pincho_uno.rectangulo.x + 48, piso_principal.rectangulo.top - 21)
        pincho_tres = Trampa("Recursos/items/spike.png", (48,21), pincho_dos.rectangulo.x + 48, piso_principal.rectangulo.top - 21)

        lista_pinchos.append(pincho_uno)
        lista_pinchos.append(pincho_dos)
        lista_pinchos.append(pincho_tres)

        #SNITCH
        x_inicial_snitch = W - 100
        y_inicial_snitch = piso_tres.rectangulo.y - 30

        imagen_snitch = pygame.image.load("Recursos/fotos/snitch_2.png")

        snitch = Secundario(x_inicial_snitch, y_inicial_snitch, imagen_snitch, None, 0)

        # #HECHIZO

        lista_imagenes_hechizo = [hechizo_harry, hechizo_harry_izquierda]
        reescalar_imagen(lista_imagenes_hechizo, 30, 30)

        #ARAÑA        
        velocidad_araña = 10

        lista_animaciones_araña = [araña_derecha, araña_izquierda, araña_herida]

        reescalar_imagen(lista_animaciones_araña, 32, 20)

        araña_uno = Enemigo(x_piso_dos, piso_dos.rectangulo.top - 27, araña_derecha[0], "Recursos/sonidos/araña.wav", velocidad_araña, araña_derecha, araña_izquierda, araña_herida)
        araña_dos = Enemigo(x_piso_uno + 50, piso_uno.rectangulo.top - 27, araña_derecha[0], "Recursos/sonidos/araña.wav", velocidad_araña, araña_derecha, araña_izquierda, araña_herida)
        araña_tres = Enemigo(x_piso_tres + 50, piso_tres.rectangulo.top - 27, araña_derecha[0], "Recursos/sonidos/araña.wav", velocidad_araña, araña_derecha, araña_izquierda, araña_herida)
        araña_cuatro = Enemigo(W-50, piso_principal.rectangulo.top - 25, araña_derecha[0], "Recursos/sonidos/araña.wav", velocidad_araña, araña_derecha, araña_izquierda, araña_herida)

        
        lista_enemigos = []

        lista_enemigos.append(araña_uno)
        lista_enemigos.append(araña_dos)
        lista_enemigos.append(araña_tres)
        lista_enemigos.append(araña_cuatro)
        #BARRA DE VIDA

        for imagen in barra_vida:
            pygame.transform.scale(imagen, (100,60))

        pared_uno = Plataformas("Recursos/terreno/tree.png", (45,94), piso_uno.rectangulo.x - 10, piso_uno.rectangulo.y - 94)
        lista_plataformas.append(pared_uno)
        pared_dos = Plataformas("Recursos/terreno/tree.png", (45,94), piso_dos.lados['right'].x - 25, piso_dos.rectangulo.y - 94)
        lista_plataformas.append(pared_dos)
        pared_tres = Plataformas("Recursos/terreno/tree.png", (45,94), piso_tres.rectangulo.x - 10, piso_tres.rectangulo.y - 94)
        lista_plataformas.append(pared_tres)

        super().__init__(pantalla, harry, lista_plataformas, fondo, snitch, lista_enemigos, 60, lista_pinchos, "dos", "Recursos/sonidos/nivel_2.wav")