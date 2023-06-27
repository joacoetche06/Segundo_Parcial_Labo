from Clase_Personaje import Personaje
from Clase_Proyectiles import Hechizo
from configuraciones import hechizo_voldemort, voldemort_quieto

class Voldemort(Personaje):
    def __init__(self, x, y, imagen, path_sonido, velocidad):
        super().__init__(imagen, x, y, path_sonido, velocidad)
        self.bandera = False
        self.lista_hechizos_voldemort = []
        self.vida = 3
        self.bandera_sonido = False

    def animar_imagen(self, pantalla, rectangulo, accion):
        if rectangulo != None: 
            largo = len(accion)
            if self.contador_pasos >= largo:
                self.contador_pasos = 0
            pantalla.blit(accion[self.contador_pasos], rectangulo)
            self.contador_pasos += 1    

    def atacar(self, pantalla, animacion, personaje):
        print(self.bandera)
        if self.bandera == True:
            self.animar_imagen(pantalla, self.rectangulo, animacion)
            self.hechizo = Hechizo(self.lados['right'].x - 100, self.lados['right'].y + 25, hechizo_voldemort[0],"Recursos/voldemort/avadakadavra.OGG",15, self.lista_hechizos_voldemort)
            self.lista_hechizos_voldemort.append(self.hechizo)
            #self.hechizo.mover_proyectil_enemigo(personaje, self, pantalla)
            try:
                if self.bandera_sonido == False:
                    self.lista_hechizos_voldemort[0].sonido.play()
                    self.bandera = True
                self.bandera_sonido = True
            except:
                print("Error voldy")
        else:
            self.animar_imagen(pantalla, self.rectangulo, voldemort_quieto)
            self.bandera_sonido = False

    def verificar_colision_hechizo_harry(self, lista_hechizos):
        for hechizo in lista_hechizos:
            if self.rectangulo.colliderect(hechizo.rectangulo):
                self.vida -= 1
                hechizo.desaparecer_proyectil(hechizo)

