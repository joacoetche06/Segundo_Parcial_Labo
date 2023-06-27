import pygame
from movimiento import obtener_rectangulos
from configuraciones import personaje_ataca, personaje_camina, personaje_camina_izquierda, personaje_quieto, personaje_salta



class Personaje:

    def __init__(self, imagen, x, y, path_sonido, velocidad):
        self.superficie = imagen
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y
        self.que_hace = "Quieto"
        self.lados = obtener_rectangulos(self.rectangulo)
        self.lados['right'].height -= 15
        self.lados['left'].height -= 15
        if path_sonido != None:
            self.sonido = pygame.mixer.Sound(path_sonido)
            self.sonido.set_volume(0.2)
        self.velocidad = velocidad
        self.puntaje = 0
        self.vida = 5
        self.colision_derecha = False
        self.colision_izquierda = False
        self.esta_saltando = False
        self.desplazamiento_y = 0
        self.gravedad = 1
        self.limite_velocidad_caida = 15
        self.potencia_salto = -15
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

    def aplicar_gravedad(self,pantalla, plataformas:list):
        bandera = False
        if self.esta_saltando:
            bandera = True
            self.animar_imagen(pantalla, self.lados['main'], personaje_salta)
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

        retorno = self.verificar_colision_plataforma(plataformas, bandera)
        
        return retorno

    def verificar_colision_plataforma(self, plataformas, comienzo):
        retorno = False
        for plataforma in plataformas:
            if self.lados["bottom"].colliderect(plataforma.lados["top"]):
                self.esta_saltando = False
                self.desplazamiento_y = 0
                self.lados['main'].bottom = plataforma.lados['main'].top + 5
                retorno = True
                break
            elif self.lados["top"].colliderect(plataforma.lados["bottom"]):
                self.lados['main'].top = plataforma.lados['main'].bottom - 2
                self.desplazamiento_y = self.gravedad
            elif self.lados["right"].colliderect(plataforma.lados["left"]):
                self.colision_derecha = True
                self.colision_izquierda = False
            elif self.lados["left"].colliderect(plataforma.lados["right"]):
                self.colision_derecha = False
                self.colision_izquierda = True
            elif comienzo or self.rectangulo.y < 455:  # Verificar si comienzo es True
                self.esta_saltando = True
            else:
                self.esta_saltando = False
                retorno = True
                self.desplazamiento_y += self.gravedad        
        return retorno

    def verificar_colision_enemigo(self, pantalla, lista_enemigos):
        for enemigo in lista_enemigos:
            if self.rectangulo.colliderect(enemigo.rectangulo):
                self.vida -= 1
                enemigo.desaparecer_enemigo(pantalla, enemigo)

    def mover_personaje(self, pantalla, lista_plataformas):
        match self.que_hace:
            case "Derecha":
                if not self.esta_saltando:
                    self.animar_imagen(pantalla, self.lados['main'], personaje_camina)
                self.mover_imagen(self.lados, self.velocidad)
            case "Izquierda":
                if not self.esta_saltando:
                    self.animar_imagen(pantalla, self.lados['main'], personaje_camina_izquierda)
                self.mover_imagen(self.lados, -self.velocidad)
            case "Salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            case "Quieto":
                if not self.esta_saltando:
                    self.animar_imagen(pantalla, self.lados['main'], personaje_quieto)
            case "Ataca":
                if not self.esta_saltando:
                    self.animar_imagen(pantalla, self.lados['main'], personaje_ataca)
        
        retorno = self.aplicar_gravedad(pantalla, lista_plataformas)

        return retorno
