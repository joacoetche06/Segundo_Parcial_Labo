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
from base_de_datos import *

bandera = False

class FormPrincipal(Form):
    def __init__(self, screen, x, y, w, h,color_background, color_border = "Black", border_size = -1, active = True, puntaje = 0):
        super().__init__(screen, x, y, w, h,color_background, color_border, border_size, active)

        self.volumen = 0.2
        self.flag_play = True #para que se reproduzca el sonido
        self.nombre = ""
        self.puntaje = puntaje
        pygame.mixer.init()

        ###CONTROLES#########
        self.txtbox = TextBox(self._slave, x, y, 125, 340, 150, 30, "Gray", "White", "Red", "Blue", 2, font = "Comic Sans", font_size = 15, font_color = "Black")
        #self.btn_music = Button(self._slave, x, y, 70, 140, 80, 50, "Green", "Blue", self.btn_music_click, "Nombre", "On", font="Verdana", font_size = 15, font_color = "Red")
        self.btn_music =Button_Image(self._slave, x, y, 80, 140, 60, 60, path_image="Recursos/items/music_on.png", onclick= self.btn_music_click, onclick_param=["Recursos/items/music_off.png","Recursos/items/music_on.png"])
        self.btn_sound =Button_Image(self._slave, x, y, 220, 140, 60, 60, path_image="Recursos/items/2.png", onclick= self.btn_sound_click, onclick_param=["Recursos/items/1.png","Recursos/items/2.png"])
        self.label_volumen =Label(self._slave, 340, 140, 80, 50, "20%", font = "Comic Sans", font_size = 15, font_color = "Black", path_image = "Recursos/items/Gray.png")
        self.slider_volumen = Slider(self._slave, x, y, 125, 260, 250, 15, self.volumen, "Blue", "White")
        # self.btn_tabla = Button_Image(self._slave, x, y, 400, 300, 100, 50, path_image="API_FORMS/Menu_BTN.png", onclick= self.btn_tabla_click, onclick_param="opcional")
        self.btn_tabla = Button(self._slave, x, y, 300, 330, 75, 50, "Black", "Red", self.btn_tabla_click, "Nombre", "Score", font="Verdana", font_size = 15, font_color = "White")
        self.btn_play = Button(self._slave, x, y, 210, 440, 75, 50, "Red", "Red", self.btn_play_click, "Nombre", "Play", font="Verdana", font_size = 15, font_color = "White")
        self.picture_box = PictureBox(self._slave, 150, 20, 200, 80, path_image = "Recursos/modelo/logo.png")
        ###

        #agrego los controles a la lista
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_music)
        self.lista_widgets.append(self.btn_sound)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.picture_box)


        pygame.mixer.music.load("Recursos/sonidos/harry_potter_theme.mp3")

        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

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
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos, bandera)
            

    
    def render(self):
        self._slave.fill(self._color_background)

    def btn_music_click(self, lista):
        if self.flag_play:
            pygame.mixer.music.pause()
            aux_image = pygame.image.load(lista[0])
            aux_image = pygame.transform.scale(aux_image,(60,60))
            self.btn_music._slave = aux_image
        else:
            pygame.mixer.music.unpause()
            aux_image = pygame.image.load(lista[1])
            aux_image = pygame.transform.scale(aux_image,(60,60))
            self.btn_music._slave = aux_image

        self.flag_play = not self.flag_play

    def btn_sound_click(self, lista):
        global bandera
        if self.flag_play:
            bandera = "Hola"
            aux_image = pygame.image.load(lista[0])
            aux_image = pygame.transform.scale(aux_image,(60,60))
            self.btn_sound._slave = aux_image
        else:
            bandera = "Chau"
            aux_image = pygame.image.load(lista[1])
            aux_image = pygame.transform.scale(aux_image,(60,60))
            self.btn_sound._slave = aux_image

        self.flag_play = not self.flag_play

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def btn_tabla_click(self, texto):
        # dic_score = [{"Jugador": "Gio", "Score": 1000},
        # {"Jugador": "Fausto", "Score": 100},
        # {"Jugador": "Gonza", "Score": 150}]
        self.nombre = self.txtbox.get_text()
        if self.nombre == "":
            print("Ingrese su nombre")
        else:
            dic_score = crear_base_de_datos(self.nombre, self.puntaje)
            print(dic_score)
            form_puntaje = FormMenuScore(self._master, 400, 25, 500, 550, (220,0,220), "White",True, "Recursos/modelo/fondo_tabla.jpg", dic_score, 100, 10, 10)
            self.show_dialog(form_puntaje)
        


    def btn_play_click(self, texto):
        
        form_jugar = FormMenuLevels(screen=self._master, 
        x = self._master.get_width() / 2 -250, y = self._master.get_height() / 2 - 250, w=500,h=500,color_background = (220,0,220), color_border=(255,255,255),active=True,path_image="Recursos/modelo/fondo_tabla.jpg")
        self.show_dialog(form_jugar)
    
    def fondo(self, path, ancho, alto):
        background_image = pygame.image.load(path)
        background_image = pygame.transform.scale(background_image, (ancho, alto))
        background_surface = pygame.Surface((100, 100))
        for y in range(0, alto, background_image.get_height()):
            for x in range(0, ancho, background_image.get_width()):
                background_surface.blit(background_image, (x, y))