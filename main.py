import pygame, sys, time, random



# from Clase_Personaje import *
# from Clase_Plataforma import *
# from Clase_Proyectiles import *
# from Clase_Enemigo import *
# from Clase_Secundario import *

from GUI_form_principal import *
from API_FORMS.GUI_form_menu_fin import *


# from niveles.nivel import Nivel

#PANTALLA
W, H = 1300, 700
FPS = 18
# nombre = input("Ingrese su nombre: ")
# if nombre != "":
pygame.init()
RELOJ = pygame.time.Clock()

PANTALLA = pygame.display.set_mode((W,H))
fondo_pantalla_carga = pygame.image.load("Recursos/fotos/pantalla_carga.jpg")
fondo_pantalla_carga = pygame.transform.scale(fondo_pantalla_carga, (W,H))
#SALTO

#FORM PRUEBA

nombre = "joa"

form_prueba = FormPrincipal(PANTALLA, 400, 115, 500, 430, "dimgrey", "black", 5, True, nombre, puntaje=0, sonido = "Recursos/sonidos/harry_potter_theme.mp3")


while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    PANTALLA.blit(fondo_pantalla_carga, (0,0))   
    
    form_prueba.update(eventos)

    pygame.display.flip()