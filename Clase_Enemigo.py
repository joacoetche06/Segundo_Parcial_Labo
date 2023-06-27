import pygame, random

from Clase_Personaje import Personaje



class Enemigo(Personaje):
    def __init__(self, x, y, imagen, path_sonido, velocidad, movimiento_derecha, movimiento_izquierda, movimiento_desaparicion):
        super().__init__(imagen, x, y, path_sonido, velocidad)
        self.bandera = True
        self.movimiento_derecha = movimiento_derecha
        self.movimiento_izquierda = movimiento_izquierda
        self.movimiento_desaparicion = movimiento_desaparicion

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

    def mover_enemigo(self, pantalla,lista_enemigos, plataformas):
        self.lista_enemigos = lista_enemigos
        
        if self.rectangulo.x < pantalla.get_width() - self.velocidad and self.bandera == True:
            self.animar_imagen(pantalla, self.rectangulo, self.movimiento_derecha)
            self.mover_imagen(self.lados, self.velocidad)
            for plataforma in plataformas:
                if (self.rectangulo.colliderect(plataforma.rectangulo) or 
                    self.rectangulo.x > pantalla.get_width() - self.velocidad - self.rectangulo.width
                    #or self.rectangulo.colliderect(pared_dos.rectangulo)
                    ):
                    self.bandera = False
        elif self.bandera == False:
            self.animar_imagen(pantalla, self.rectangulo, self.movimiento_izquierda)
            self.mover_imagen(self.lados, -self.velocidad)
            for plataforma in plataformas:
                if (self.rectangulo.colliderect(plataforma.rectangulo) or self.rectangulo.x < self.velocidad
                    #or self.rectangulo.colliderect(pared.rectangulo) 
                    #or self.rectangulo.colliderect(pared_tres.rectangulo)
                    ):
                    self.bandera = True

    
    def desaparecer_enemigo(self, pantalla, enemigo):
        self.animar_imagen(pantalla, self.rectangulo, self.movimiento_desaparicion)
        self.lista_enemigos.remove(enemigo)
        if self.sonido != None:
            self.sonido.play()


