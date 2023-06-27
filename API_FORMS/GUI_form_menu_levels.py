import pygame
from pygame.locals import *

from API_FORMS.GUI_button_image import *
from API_FORMS.GUI_form import *
from API_FORMS.GUI_label import *
from API_FORMS.GUI_form_contenedor_niveles import *
from API_FORMS.GUI_form_inicio import *
from niveles.manejador_niveles import Manejador_niveles

class FormMenuLevels(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image):
        super().__init__(screen, x, y, w, h, color_background, color_border, -1, active)
        self.manejador_niveles = Manejador_niveles(self._master)
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen

        self._btn_level_1 = Button_Image(screen=self._slave, x=120, y = 100, master_x=x, master_y=y,w =100,h=150,onclick=self.entrar_nivel,onclick_param="nivel_uno",path_image="Recursos/items/01.png")

        self._btn_level_2 = Button_Image(screen=self._slave, x=270, y = 100, master_x=x, master_y=y,w =100,h=150,onclick=self.entrar_nivel,onclick_param="nivel_dos",path_image="Recursos/items/02.png")

        self._btn_level_3 = Button_Image(screen=self._slave, x=200, y = 300, master_x=x, master_y=y,w =100,h=150,onclick=self.entrar_nivel,onclick_param="nivel_tres",path_image="Recursos/items/03.png")

        self._btn_home = Button_Image(screen=self._slave, x=400, y = 400, master_x=x, master_y=y,w =50,h=50,onclick=self.btn_home_click,onclick_param="",path_image="API_FORMS/home.png")

        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self._btn_level_1)
        self.lista_widgets.append(self._btn_level_2)
        self.lista_widgets.append(self._btn_level_3)

    def on(self, parametro):
        print("hola", parametro)

    def update(self, lista_eventos, bandera_sonidos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
                self.draw()
        else:
            retorno = self.hijo.update(lista_eventos, bandera_sonidos)
            if retorno == True:
                form_contenedor_nivel = FormContenedorNiveles(self._master, self.nivel)
                self.show_dialog(form_contenedor_nivel)
            
    def entrar_nivel(self, nombre_nivel):
        self.nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        form_menu = FormInicio(self._master, 450, 25, 400, 200, (220,0,220), "White", True, "Recursos/fotos/menu.jpg", 10, nombre_nivel)
        self.show_dialog(form_menu)
        

    def btn_home_click(self, param):
        self.end_dialog()