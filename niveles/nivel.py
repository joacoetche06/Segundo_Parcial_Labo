import pygame, time, sys, pygame.font
from pygame.locals import *

from Clase_Proyectiles import Hechizo
from modo import *
from funciones import dibujar_cuadrados
from configuraciones import piso_nivel_uno
from API_FORMS.GUI_form_menu_levels import *

#################no estoy seguro si va aca
from configuraciones import personaje_salta, fenix_volando, fenix_volando_izquierda, duende_volando, duende_volando_izquierda, barra_vida, hechizo_harry, voldemort_izquierda, cabeza_vida_voldemort, voldemort_caido
#################

atacando = False
presionada= True

tiempo = 0

bandera_sonido_hechizo = True
bandera_enemigo = True

# gravedad = 1




tiempo_total = 5  # tiempo total en segundos
tiempo_restante = tiempo_total  # tiempo restante inicialmente igual al tiempo total
temporizador_tiempo_anterior = pygame.time.get_ticks()
temporizador_tick = 1000  # Actualización cada segundo (en milisegundos)




#10 minutos del video
class Nivel:
    def __init__(self, pantalla, personaje, lista_plataformas, fondo, fruta, lista_enemigos, tiempo_total, voldemort = None):
        self._slave = pantalla
        self.jugador = personaje
        self.plataformas = lista_plataformas
        self.imagen_fondo = fondo
        self.fruta = fruta
        self.lista_enemigos = lista_enemigos
        self.lista_hechizos = []
        self.bandera_fin = False
        self.tiempo_total = tiempo_total
        self.tiempo_restante = self.tiempo_total
        self.temporizador_tiempo_anterior = pygame.time.get_ticks()
        self.voldemort = voldemort
        self.lista_hechizos_voldemort = []
        self.bandera_muerte = False

    def update(self, lista_eventos, bandera_sonidos):
        bandera_tiempo = False
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
            
        
        retorno = self.actualizar_pantalla()
        self.leer_inputs(retorno)
        self.dibujar_rectangulos()
        self.actualizar_vida(self._slave)
        if self.voldemort != None:
            self.actualizar_vida_voldemort(self._slave)
        self.recibir_bandera_sonidos(bandera_sonidos)
        bandera_fin = self.verificar_fin()
        bandera_tiempo = self.temporizar()
        retorno = False
        # if bandera_tiempo == True:
        #     form_jugar = FormMenuLevels(screen=self._slave, 
        #     x = self._slave.get_width() / 2 -250, y = self._slave.get_height() / 2 - 250,
        #     w=500,h=500,color_background = (220,0,220), color_border=(255,255,255),active=True,path_image="Recursos/modelo/fondo_tabla.jpg")
        #     form_jugar.update(lista_eventos, retorno)
# ARREGLARLO           self.end_dialog()

        return retorno

    def verificar_fin(self):
        if self.fruta.rectangulo == None and len(self.lista_enemigos) == 0:
            self.bandera_fin = True
        return self.bandera_fin


    def recibir_bandera_sonidos(self, bandera):
        if bandera:
            for hechizo in self.lista_hechizos:
                self.jugador.sonido = None
                self.fruta.sonido = None
                for enemigo in self.lista_enemigos:
                    enemigo.sonido = None
                hechizo.sonido = None
            

    def actualizar_pantalla(self):
        global bandera_sonido_hechizo, atacando, bandera_enemigo
        
        self._slave.blit(self.imagen_fondo, (0,0))
        for plataforma in self.plataformas:
            self._slave.blit(plataforma.superficie, (plataforma.rectangulo.x, plataforma.rectangulo.y))

        if self.fruta.rectangulo != None:
            if self.fruta.velocidad != 0:
                self.fruta.mover_secundario(self._slave, fenix_volando, fenix_volando_izquierda)
                self.fruta.rectangulo = self.fruta.verificar_colision(self.jugador, self.fruta.sonido)
            else:
                self._slave.blit(self.fruta.superficie, (self.fruta.rectangulo.x, self.fruta.rectangulo.y))
                self.fruta.rectangulo = self.fruta.verificar_colision(self.jugador, None)
        else:
            if self.voldemort != None:
                self.voldemort.bandera = True


        for enemigo in self.lista_enemigos:
            if enemigo.rectangulo != None:
                enemigo.mover_enemigo(self._slave,
                self.lista_enemigos, self.plataformas)
        else:
            bandera_sonido_hechizo = True
            
        if len(self.lista_hechizos) > 0:
            self.lista_hechizos[0].mover_proyectil_personaje(self.jugador,atacando, self._slave)
            if self.lista_hechizos[0].rectangulo != None:
                atacando = self.lista_hechizos[0].verificar_colision_proyectil(self.plataformas,
                self._slave.get_width(), atacando, self.lista_enemigos, self.jugador, self._slave)
            bandera_sonido_hechizo = True
        retorno = self.jugador.mover_personaje(self._slave, self.plataformas)


        if self.voldemort != None and self.bandera_muerte == False:
            self.voldemort.atacar(self._slave, voldemort_izquierda, self.jugador)
            # self.voldemort.verificar_colision_hechizo_harry(self.lista_hechizos)
            if len(self.voldemort.lista_hechizos_voldemort) > 0:
                self.voldemort.lista_hechizos_voldemort[0].mover_proyectil_enemigo(self.jugador, self.voldemort, self._slave, self.voldemort.bandera)
                self.voldemort.bandera = False
        return retorno
    


    def leer_inputs(self, bandera_sonido_salto):
        global atacando, presionada, tiempo, bandera_sonido_hechizo

        keys = pygame.key.get_pressed()


    #SOLUCIONAR COLISION CON PLATAFORMAS
        if (keys[pygame.K_RIGHT] and 
            self.jugador.rectangulo.x < self._slave.get_width() - self.jugador.velocidad - self.jugador.rectangulo.width
            and self.jugador.colision_derecha == False):
            self.jugador.que_hace = "Derecha"
        elif (keys[pygame.K_LEFT] and self.jugador.rectangulo.x > 0 + self.jugador.velocidad
            and self.jugador.colision_izquierda == False):
            self.jugador.que_hace = "Izquierda"
        elif keys[pygame.K_UP] and presionada == True:                
            self.jugador.que_hace = "Salta"
            presionada = False
            if bandera_sonido_salto == True:
                bandera_sonido_salto = False
                if self.jugador.sonido != None:
                    self.jugador.sonido.play()
        elif keys[pygame.K_SPACE] and presionada == True and len(self.lista_hechizos) < 1:
            tiempo = time.time()
            self.jugador.que_hace = "Ataca"
            atacando = True
            presionada = False
            hechizo = Hechizo(self.jugador.lados['right'].x + 25, self.jugador.lados['right'].y + 25, hechizo_harry[0], "Recursos/sonidos/incendio.wav", 15, self.lista_hechizos)
            self.lista_hechizos.append(hechizo)
            try:
                # if self.hechizos[0].sonido == None:
                #     print("hola")
                if bandera_sonido_hechizo == True:  
                    self.lista_hechizos[0].sonido.play()
                bandera_sonido_hechizo = False
            except:
                print("Error")
        elif time.time() - 0.2 > tiempo:
            self.jugador.que_hace = "Quieto"
            presionada = True
            self.jugador.colision_derecha = False
            self.jugador.colision_izquierda = False
        

    def dibujar_rectangulos(self):
        if get_mode():
            for plataforma in self.plataformas:
                dibujar_cuadrados(self._slave, plataforma.lados, "Green")
            dibujar_cuadrados(self._slave, self.jugador.lados, "Black")
            dibujar_cuadrados(self._slave, self.fruta.lados, "Green")
            for hechizo in self.lista_hechizos:
                dibujar_cuadrados(self._slave, hechizo.lados, "White")
            for enemigo in self.lista_enemigos:
                dibujar_cuadrados(self._slave, enemigo.lados, "Brown")
            if self.voldemort != None:
                dibujar_cuadrados(self._slave, self.voldemort.lados, "Red")

    def actualizar_vida_voldemort(self, pantalla):
        
        self.voldemort.verificar_colision_hechizo_harry(self.lista_hechizos)
        if self.voldemort.vida == 3:
            pantalla.blit(cabeza_vida_voldemort, (30, 620))
            pantalla.blit(cabeza_vida_voldemort, (90, 620))
            pantalla.blit(cabeza_vida_voldemort, (150, 620))
        elif self.voldemort.vida == 2:
            pantalla.blit(cabeza_vida_voldemort, (30, 620))
            pantalla.blit(cabeza_vida_voldemort, (90, 620))
        elif self.voldemort.vida == 1:
            pantalla.blit(cabeza_vida_voldemort, (30, 620))
        else:
            pass
            #PANTALLA DE VICTORIA

    def actualizar_vida(self, PANTALLA):
        pygame.font.init()
        x =1100
        y = 635
        fuente_score = pygame.font.SysFont("Harry P", 50)
        puntaje = fuente_score.render("SCORE: {0}" .format(self.jugador.puntaje), True, (255, 0, 0))
        PANTALLA.blit(puntaje, (0,0))
        
        self.jugador.verificar_colision_enemigo(PANTALLA, self.lista_enemigos)
        
        
        match self.jugador.vida:
            case 5:
                PANTALLA.blit(barra_vida[0], (x,y))
            case 4:
                PANTALLA.blit(barra_vida[1], (x,y))
            case 3:
                PANTALLA.blit(barra_vida[2], (x,y))
            case 2:
                PANTALLA.blit(barra_vida[3], (x,y))
            case 1:
                PANTALLA.blit(barra_vida[4], (x,y))
            case 0:
                PANTALLA.blit(barra_vida[5], (x,y))
                pygame.quit()
                sys.exit(0)
                #tendria que ir a una pantalla de menu

    def temporizar(self):
        global  temporizador_tick
        termino = False
        #ARREGLAR TIEMPO DESPUES QUE TERMINE
        
        pygame.font.init()
        fuente_temporizador = pygame.font.SysFont("Times New Roman", 50)
        tiempo_actual = pygame.time.get_ticks()

        tiempo_transcurrido = tiempo_actual - self.temporizador_tiempo_anterior
        if tiempo_transcurrido >= temporizador_tick:
            self.tiempo_restante -= 1
            if self.tiempo_restante <= 0:
                termino = True
                self.tiempo_restante = 0
            self.temporizador_tiempo_anterior = tiempo_actual

        minutos = self.tiempo_restante // 60
        segundos = self.tiempo_restante % 60

        temporizador = fuente_temporizador.render(f"{minutos:02}:{segundos:02} hola", True, (255, 0, 0), "White")

        self._slave.blit(temporizador, (1187,1))

        return termino
    
    