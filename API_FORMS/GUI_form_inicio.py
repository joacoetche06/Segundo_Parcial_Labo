import pygame
from pygame.locals import *

from API_FORMS.GUI_button_image import *
from API_FORMS.GUI_form import *
from API_FORMS.GUI_label import *
# from API_FORMS.GUI_form_contenedor_niveles import *
# from GUI_form_principal import *


class FormInicio(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image, margen_x, nivel):
        super().__init__(screen, x, y, w, h, color_background, color_border, -1,active)
        self.nivel = nivel
        self.bandera = False

        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen
        match self.nivel:
            case "nivel_uno":
                self.texto_uno = "Elimina todos las dixies y"
                self.texto_dos = "libera al fenix para avanzar."
                self.texto_tres = None
            case "nivel_dos":
                self.texto_uno = "Elimina todos las arañas y"
                self.texto_dos = "encuentra la snitch para avanzar."
                self.texto_tres = None
            case "nivel_tres":
                self.texto_uno = "Elimina todos las serpientes y"
                self.texto_dos = "encuentra la piedra de la resurreccion"
                self.texto_tres = "para vencer a Lord Voldemort."

        self.label_texto_uno =Label(self._slave, 10, 30, 380, 20, self.texto_uno, font = "Comic Sans", font_size = 15, font_color = "White", path_image = "")
        self.label_texto_dos =Label(self._slave, 10, 50, 380, 20, self.texto_dos, font = "Comic Sans", font_size = 15, font_color = "White", path_image = "")

        self.btn_play = Button(self._slave, x, y, 175, 150, 50, 25, "Red", "Red", self.btn_play_click, "Nombre", "Play", font="Verdana", font_size = 15, font_color = "White")

        self.lista_widgets.append(self.label_texto_uno)
        self.lista_widgets.append(self.label_texto_dos)
        if self.texto_tres != None:
            self.label_texto_tres =Label(self._slave, 10, 70, 380, 20, self.texto_tres, font = "Comic Sans", font_size = 15, font_color = "White", path_image = "")
            self.lista_widgets.append(self.label_texto_tres)
        self.lista_widgets.append(self.btn_play)

        self._btn_home = Button_Image(screen=self._slave, x=w-55, y = h-55, master_x=x, master_y=y,w =35,h=35,color_background=(255,0,0), color_border=(255,0,255),onclick=self.btn_home_click,onclick_param="",text="",font="Verdana", font_size =15, font_color=(0,255,0),path_image="API_FORMS/home.png")
        self.lista_widgets.append(self._btn_home)

    def update(self, lista_eventos):
        if self.active:
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        return self.bandera
    
    def btn_play_click(self, texto):
        self.bandera = True
        pygame.mixer.music.pause()

    def btn_home_click(self, param):
        self.end_dialog()
        # self.end_dialog()
        # form_contenedor_nivel = FormContenedorNiveles(self._master, self.nivel)
        # self.show_dialog(form_contenedor_nivel)




