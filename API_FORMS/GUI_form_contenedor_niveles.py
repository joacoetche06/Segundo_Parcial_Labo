import pygame
from pygame.locals import *

from API_FORMS.GUI_button_image import *
from API_FORMS.GUI_form import *

class FormContenedorNiveles(Form):
    def __init__(self, pantalla: pygame.Surface, nivel):
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height())
        nivel._slave = self._slave
        self.nivel = nivel
        
        self._btn_home = Button_Image(screen=self._slave, x=self._w -50, y = 70, master_x= self._x, master_y=self._y,w =50,h=50,color_background=(255,0,0), color_border=(255,0,255),onclick=self.btn_home_click,onclick_param="",text="",font="Verdana", font_size =15, font_color=(0,255,0),path_image="API_FORMS/home.png")

        self.lista_widgets.append(self._btn_home)
    
    def update(self, lista_eventos,bandera_sonidos):
        bandera = self.nivel.update(lista_eventos, bandera_sonidos)
        for widget in self.lista_widgets:
            widget.update(lista_eventos)
        self.draw()
        return bandera
        
    def btn_home_click(self, param):
        self.end_dialog()