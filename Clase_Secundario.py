import pygame
from Clase_Personaje import Personaje


class Secundario(Personaje):
    def __init__(self, x, y, imagen, path_sonido, velocidad):
        super().__init__(imagen, x, y, path_sonido, velocidad)
        self.bandera = True
        self.contador_pasos = 0

    def mover_imagen(self, rectangulo: pygame.rect, velocidad):
        for lado in rectangulo:
            rectangulo[lado].x += velocidad

    def animar_imagen(self, pantalla, rectangulo, accion):
        if rectangulo != None: 
            largo = len(accion)
            if self.contador_pasos >= largo:
                self.contador_pasos = 0
            pantalla.blit(accion[self.contador_pasos], rectangulo)
            self.contador_pasos += 1

    def mover_secundario(self, pantalla, movimiento_derecha, movimiento_izquierda):
        if self.rectangulo.x < pantalla.get_width() - self.velocidad and self.bandera == True:
            self.animar_imagen(pantalla, self.rectangulo, movimiento_derecha)
            self.mover_imagen(self.lados, self.velocidad)
            if self.rectangulo.x > pantalla.get_width() - self.velocidad - self.rectangulo.width:
                self.bandera = False
        elif self.bandera == False:
            self.animar_imagen(pantalla, self.rectangulo, movimiento_izquierda)
            self.mover_imagen(self.lados, -self.velocidad)
            if self.rectangulo.x < self.velocidad:
                self.bandera = True
        

    def verificar_colision(self, harry, sonido):
        if harry.rectangulo.colliderect(self.rectangulo):
            
            self.rectangulo = None
            self.lados = None
            if sonido != None:
                sonido.play()
            if harry.vida < 5:
                harry.vida += 1
        return self.rectangulo