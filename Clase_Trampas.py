from Clase_Plataforma import *

class Trampa(Plataformas):
    def __init__(self, imagen, tamaño: tuple, x, y):
        super().__init__(imagen, tamaño, x, y)
        self.daño = 1
        self.bandera = True

    def verificar_colision(self, personaje):
        if self.rectangulo.colliderect(personaje.rectangulo) and self.bandera == True:
            personaje.vida -= self.daño
            self.bandera = False
        elif not self.rectangulo.colliderect(personaje.rectangulo):
            self.bandera = True

