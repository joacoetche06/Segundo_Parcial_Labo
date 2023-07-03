import pygame, sys
from pygame.locals import *


from API_FORMS.GUI_button import *
from API_FORMS.GUI_button_image import *
from API_FORMS.GUI_form import *
from API_FORMS.GUI_label import *
from API_FORMS.GUI_slider import *
from API_FORMS.GUI_textbox import *
from API_FORMS.GUI_widget import *
from API_FORMS.GUI_form_menu_score import *
from API_FORMS.GUI_picture_box import *
from API_FORMS.GUI_form_menu_levels import *
from API_FORMS.GUI_form_settings import *
from base_de_datos import *

bandera = False

class FormPrincipal(Form):
    def __init__(self, screen, x, y, w, h,color_background, color_border = "Black", border_size = -1, active = True, nombre = "", puntaje = 0, sonido = None):
        super().__init__(screen, x, y, w, h,color_background, color_border, border_size, active)

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.volumen = 0.2
        self.flag_play = True #para que se reproduzca la musica
        self.flag_sonidos = True
        self.nombre = nombre
        self.puntaje = puntaje
        self.sonido = sonido
        # self.form_settings = FormSettings(self._master, x, y, w, h, "dimgrey", "black", 5,True, self.volumen)
        self.dic_score = agregar_a_base_de_datos(self.nombre, self.puntaje)
        pygame.mixer.init()

        ###CONTROLES#########
        self.txtbox = TextBox(self._slave, x, y, 125, 340, 150, 30, "Gray", "White", "Red", "Blue", 2, font = "Comic Sans", font_size = 15, font_color = "Black")
        self.picture_box = PictureBox(self._slave, 150, 30, 200, 80, path_image = "Recursos/modelo/logo.png")
        self.btn_play = Button(self._slave, x, y, 175, 140, 150, 50, "Gray", "Red", self.btn_play_click, "Nombre", "Play", font="Verdana", font_size = 15, font_color = "Black")
        self.btn_settings =  Button(self._slave, x, y, 175, 240, 150, 50, "Gray", "Red", self.btn_settings_click, "Nombre", "Settings", font="Verdana", font_size = 15, font_color = "Black")
        self.btn_tabla = Button(self._slave, x, y, 175, 340, 150, 50, "Gray", "Red", self.btn_tabla_click, "Nombre", "Score", font="Verdana", font_size = 15, font_color = "Black")
        ###
        
        self.lista_widgets.append(self.picture_box)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.btn_settings)


        pygame.mixer.music.load(self.sonido)

        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)
        print("Empieza la musica")

        self.render()
        # self.fondo("Recursos/modelo/logo_2.png", w, h)

    def update(self, lista_eventos):
        global bandera
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                
        else:
            self.hijo.update(lista_eventos, bandera)

    
    def render(self):
        self._slave.fill(self._color_background)


    def btn_tabla_click(self, texto):
        # dic_score = [{"Jugador": "Gio", "Score": 1000},
        # {"Jugador": "Fausto", "Score": 100},
        # {"Jugador": "Gonza", "Score": 150}]
        # if self.nombre == "":
        #     print("Ingrese su nombre")
        # else:
        form_puntaje = FormMenuScore(self._master, 400, 25, 500, 550, (220,0,220), "White",True, "Recursos/modelo/fondo_tabla.jpg", self.dic_score, 100, 10, 10)
        self.show_dialog(form_puntaje)
        


    def btn_play_click(self, texto):
        
        form_jugar = FormMenuLevels(screen=self._master, 
        x = self._master.get_width() / 2 -250, y = self._master.get_height() / 2 - 250, w=500,h=500,color_background = (220,0,220), color_border=(255,255,255),active=True,path_image="Recursos/modelo/fondo_tabla.jpg")
        # if form_jugar.nivel == "nivel_uno":
        #         self.sonido = "Recursos/sonidos/nivel_1.mp4"
        # elif form_jugar.nivel == "nivel_dos":
        #     self.sonido = "Recursos/sonidos/nivel_2.mp4"
        # else:
        #     self.sonido = "Recursos/sonidos/nivel_3.mp4"
        # self.contexto = form_jugar.contexto
        self.show_dialog(form_jugar)
    
    def btn_settings_click(self, texto):
        self.form_settings = FormSettings(self._master, self.x, self.y, self.w, self.h, "dimgrey", "black", 5, True, self.volumen, self.flag_play, self.flag_sonidos)
        self.show_dialog(self.form_settings)

