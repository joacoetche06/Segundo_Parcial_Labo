import pygame
from pygame.locals import *

from API_FORMS.GUI_button_image import *
from API_FORMS.GUI_form import *
from API_FORMS.GUI_form_menu_fin import *
from Clase_Contexto import *
# from niveles.nivel import *


class FormContenedorNiveles(Form):
    def __init__(self, pantalla: pygame.Surface, numero_nivel):
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height())
        numero_nivel._slave = self._slave
        self.nivel = numero_nivel
        self._btn_home = Button_Image(screen=self._slave, x=self._w -50, y = 70, master_x= self._x, master_y=self._y,w =50,h=50,color_background=(255,0,0), color_border=(255,0,255),onclick=self.btn_home_click,onclick_param="",text="",font="Verdana", font_size =15, font_color=(0,255,0),path_image="API_FORMS/home.png")

        self.lista_widgets.append(self._btn_home)
        
    
    def update(self, lista_eventos,bandera_sonidos):
        retorno = self.nivel.update(lista_eventos, bandera_sonidos)
        for widget in self.lista_widgets:
            widget.update(lista_eventos)
        if retorno == "Completado":
            self.salir_nivel(retorno)
        elif retorno == "Incompleto":
            self.salir_nivel(retorno)
        self.draw()
        return retorno

    def salir_nivel(self, estado):
        form_menu_fin = MenuFinNivel(self._master, 450, 25, 400, 200, (220,0,220), "White", True, "Recursos/fotos/menu.jpg", estado, self.nivel)
        self.show_dialog(form_menu_fin)
        self.end_dialog()
        
    def btn_home_click(self, param):
        self.end_dialog()