import pygame

from API_FORMS.GUI_button_image import *
from API_FORMS.GUI_label import *
from API_FORMS.GUI_form import *
from API_FORMS.GUI_form_menu_levels import *
from Clase_Contexto import *


class MenuFinNivel(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image, estado, numero_nivel):
        super().__init__(screen, x, y, w, h, color_background, color_border, -1, active)
        self.contexto = Context("",0,"")
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen
        self.estado = estado
        self.numero_nivel = numero_nivel

        if self.estado == "Completado":
            self.texto = ("Felicitaciones has completado el nivel {0}!".format(self.numero_nivel))
        else:
            self.texto = "Intentar nuevamente..."

        self.label_texto =Label(self._slave, 10, 30, 380, 20, self.texto, font = "Comic Sans", font_size = 15, font_color = "White", path_image = "")

        self.btn_play = Button(self._slave, x, y, 175, 150, 50, 25, "Red", "Red", self.btn_play_click, "Nombre", "Play", font="Verdana", font_size = 15, font_color = "White")



        self.lista_widgets.append(self.label_texto)
        self.lista_widgets.append(self.btn_play)
    
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
                self.draw()

    def btn_play_click(self, texto):
        form_jugar = FormMenuLevels(screen=self._master, 
        x = self._master.get_width() / 2 -250, y = self._master.get_height() / 2 - 250, w=500,h=500,color_background = (220,0,220), color_border=(255,255,255),active=True,path_image="Recursos/modelo/fondo_tabla.jpg")
        
        form_jugar.entrar_nivel(Context.nivel)
