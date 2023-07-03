import pygame
from movimiento import obtener_rectangulos

class Plataformas:

    def __init__(self, imagen, tamaño: tuple, x, y):
        self.imagen = imagen
        if type(imagen) == str:
            self.superficie = pygame.image.load(self.imagen)
            self.superficie = pygame.transform.scale(self.superficie, tamaño)
            self.rectangulo = self.superficie.get_rect()
        else:
            self.superficie = self.imagen
            self.rectangulo = self.superficie.get_rect()
            self.rectangulo.top = 455
        self.rectangulo.x = x
        self.rectangulo.y = y
        self.lados = obtener_rectangulos(self.rectangulo)