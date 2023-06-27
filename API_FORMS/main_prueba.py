import pygame, sys
from pygame.locals import *

from GUI_form_principal import FormPrueba

pygame.init()
WIDTH = 1200
HEIGHT = 600
FPS = 60

reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((WIDTH, HEIGHT))



form_prueba = FormPrueba(pantalla, 200, 100, 900, 350, "gold", "magenta", 5, True)

while True:
    reloj.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill("black")

    form_prueba.update(eventos)

    pygame.display.flip()