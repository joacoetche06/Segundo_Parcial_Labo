import pygame

from Clase_Personaje import Personaje
from configuraciones import hechizo_harry, hechizo_voldemort

class Hechizo(Personaje):
    def __init__(self, x, y, imagen, path_sonido, velocidad, lista):
        super().__init__(imagen, x, y, path_sonido, velocidad)
        # self.sonido = pygame.mixer.Sound(path_sonido)
        self.lista = lista

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

    def mover_proyectil_personaje(self, personaje, atacando, pantalla):
        if (personaje.que_hace == "Ataca" or atacando == True) and self.lados != None:
            self.animar_imagen(pantalla, self.rectangulo, hechizo_harry)
            self.mover_imagen(self.lados, self.velocidad)

    def verificar_colision_proyectil(self, plataformas,W, atacando, enemigos, harry, pantalla):
        for enemigo in enemigos:
            if self.rectangulo.colliderect(enemigo.rectangulo):
                enemigo.desaparecer_enemigo(pantalla, enemigo)
                atacando = False
                # self.rectangulo = None
                # self.lados = None
                if len(self.lista) > 0:
                    self.desaparecer_proyectil(self.lista[0])
                harry.puntaje += 100
        for plataforma in plataformas:
            if self.rectangulo != None and (self.rectangulo.colliderect(plataforma.rectangulo)
                or self.rectangulo.x > W - self.rectangulo.width):
                atacando = False
                if len(self.lista) > 0:
                    self.desaparecer_proyectil(self.lista[0])
            


        return atacando
    
    def mover_proyectil_enemigo(self, personaje, enemigo, pantalla, bandera):
        if enemigo.bandera == True:
            self.animar_imagen(pantalla, self.rectangulo, hechizo_voldemort)
            self.mover_imagen(self.lados, -self.velocidad)
            enemigo.bandera = False
            # enemigo.bandera_sonido = False
        self.verificar_colision_hechizo_voldemort(personaje, enemigo)
        return enemigo.bandera
    
    def verificar_colision_hechizo_voldemort(self, personaje, enemigo):
        if self.rectangulo.x < self.rectangulo.width:
            self.desaparecer_proyectil(self.lista)
        elif self.rectangulo.colliderect(personaje.rectangulo):
            self.desaparecer_proyectil(self.lista)
            personaje.vida -= 1
    def desaparecer_proyectil(self, hechizo):
        self.lista.pop(0)

