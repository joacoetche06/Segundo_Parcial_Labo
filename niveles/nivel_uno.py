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

class NivelUno(Nivel):
    def __init__(self, pantalla: pygame.surface):
        #PANTALLA
        W = pantalla.get_width()
        H = pantalla.get_height()

        #ICONO
        icono = pygame.image.load("Recursos/fotos/logo.png")
        pygame.display.set_icon(icono)

        #FONDO
        fondo = pygame.image.load("Recursos/fotos/fondo_1.png")
        fondo = pygame.transform.scale(fondo, (W,H))

        #PERSONAJE

        x_inicial = H/2 - 200
        y_inicial = W/2 - 160
        velocidad = 20
        
        pygame.mixer.init()
        


        lista_animaciones = [personaje_quieto, personaje_camina, personaje_camina_izquierda, personaje_salta,
                            personaje_ataca]


        reescalar_imagen(lista_animaciones, 42, 88)

        harry = Personaje(personaje_camina[0], x_inicial, y_inicial, "Recursos/sonidos/Ascendio1.wav", velocidad)

        #SUPERFICIE

        plataforma_uno = Plataformas("Recursos/items/plataforma_1.png", (163,22), 350, 350)
        plataforma_dos = Plataformas("Recursos/items/plataforma_1.png", (163,22), 650, 450)
        plataforma_tres = Plataformas("Recursos/items/plataforma_1.png", (163,22), 700, 250)

        superficie_piso_principal = dibujar_estructuras(W, piso_nivel_uno)
        superficie_piso_uno = dibujar_estructuras(W - 900, piso_nivel_uno)
        superficie_piso_dos = dibujar_estructuras(W - 1000, piso_nivel_uno)
        superficie_piso_tres = dibujar_estructuras(W - 900, piso_nivel_uno)

        piso_principal = Plataformas(superficie_piso_principal, (W,20), 0, harry.rectangulo.bottom - 10)
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
        pincho_uno = Trampa("Recursos/items/spike.png", (48,21), 150, piso_dos.rectangulo.top - 21)
        pincho_dos = Trampa("Recursos/items/spike.png", (48,21), pincho_uno.rectangulo.x + 48, piso_dos.rectangulo.top - 21)
        pincho_tres = Trampa("Recursos/items/spike.png", (48,21), pincho_dos.rectangulo.x + 48, piso_dos.rectangulo.top - 21)

        lista_pinchos.append(pincho_uno)
        lista_pinchos.append(pincho_dos)
        lista_pinchos.append(pincho_tres)

        #FENIX
        x_inicial_fenix = 100
        y_inicial_fenix = 20
        velocidad_fenix = 20

        lista_animaciones_fenix = [fenix_volando, fenix_volando_izquierda]

        reescalar_imagen(lista_animaciones_fenix, 60, 100)

        fenix = Secundario(x_inicial_fenix, y_inicial_fenix, fenix_volando[4],"Recursos/sonidos/fenix.mp3", velocidad_fenix)


        # #HECHIZO
        y_inicial_hechizo = harry.lados['right'].y + 25

        lista_imagenes_hechizo = [hechizo_harry, hechizo_harry_izquierda]
        reescalar_imagen(lista_imagenes_hechizo, 30, 30)

        #DUENDE
        velocidad_duende = 10

        lista_animaciones_duende = [duende_quieto, duende_volando, duende_volando_izquierda, duende_atacando, duende_herido]

        reescalar_imagen(lista_animaciones_duende, 28, 38)

        duende_uno = Enemigo(x_piso_dos, y_piso_dos - 20, duende_quieto[0], "Recursos/sonidos/goblin_death_02.ogg", velocidad_duende, duende_volando, duende_volando_izquierda, duende_herido)
        
        duende_dos = Enemigo(x_piso_uno, y_piso_uno - 20, duende_quieto[0], "Recursos/sonidos/goblin_death_02.ogg", velocidad_duende, duende_volando, duende_volando_izquierda, duende_herido)
        duende_tres = Enemigo(x_piso_tres, y_piso_tres - 20, duende_quieto[0], "Recursos/sonidos/goblin_death_02.ogg", velocidad_duende, duende_volando, duende_volando_izquierda, duende_herido)
        duende_cuatro = Enemigo(W-20, y_inicial_hechizo, duende_quieto[0], "Recursos/sonidos/goblin_death_02.ogg", velocidad_duende, duende_volando, duende_volando_izquierda, duende_herido)

        
        
        lista_enemigos = []

        lista_enemigos.append(duende_uno)
        lista_enemigos.append(duende_dos)
        lista_enemigos.append(duende_tres)
        lista_enemigos.append(duende_cuatro)
        #BARRA DE VIDA

        for imagen in barra_vida:
            pygame.transform.scale(imagen, (100,60))

        pared_uno = Plataformas("Recursos/terreno/1.png", (28,92), piso_uno.rectangulo.x - 28, piso_uno.rectangulo.y - 42)
        lista_plataformas.append(pared_uno)
        pared_dos = Plataformas("Recursos/terreno/1.png", (28,92), piso_dos.lados['right'].x, piso_dos.rectangulo.y - 42)
        lista_plataformas.append(pared_dos)
        pared_tres = Plataformas("Recursos/terreno/1.png", (28,92), piso_tres.rectangulo.x - 28, piso_tres.rectangulo.y - 42)
        lista_plataformas.append(pared_tres)

        super().__init__(pantalla, harry, lista_plataformas, fondo, fenix, lista_enemigos, 60, lista_pinchos, "Uno")

    