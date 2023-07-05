import pygame
from pygame.locals import *

from API_FORMS.GUI_button_image import *
from API_FORMS.GUI_form import *
from API_FORMS.GUI_picture_box import *
from API_FORMS.GUI_label import *
from API_FORMS.GUI_slider import *

class FormSettings(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, border_size, active, volume, bandera_musica, bandera_sonido):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        on = pygame.image.load("Recursos/items/music_on.png")
        self.on  = pygame.transform.scale(on ,(60,60))
        off = pygame.image.load("Recursos/items/music_off.png")
        self.off  = pygame.transform.scale(off ,(60,60))
        self.bandera_musica = True
        self.bandera_sonido = True
        self.volumen = volume

        self._btn_home = Button_Image(screen=self._slave, x=w-70, y = h-70, master_x=x, master_y=y,w =50,h=50,color_background=(255,0,0), color_border=(255,0,255),onclick=self.btn_home_click,onclick_param="",text="",font="Verdana", font_size =15, font_color=(0,255,0),path_image="API_FORMS/home.png")
        self.btn_music = Button_Image(self._slave, x, y, 80, 140, 60, 60, path_image= "Recursos/items/music_on.png", onclick= self.btn_music_click, onclick_param="")
        self.picture_box = PictureBox(self._slave, 150, 30, 200, 80, path_image = "Recursos/modelo/logo.png")
        self.btn_sound =Button_Image(self._slave, x, y, 220, 140, 60, 60, path_image="Recursos/items/2.png", onclick= self.btn_sound_click, onclick_param=["Recursos/items/1.png","Recursos/items/2.png"])
        self.label_volumen =Label(self._slave, 340, 140, 80, 50, "20%", font = "Comic Sans", font_size = 15, font_color = "Black", path_image = "Recursos/items/Gray.png")
        self.slider_volumen = Slider(self._slave, x, y, 125, 260, 250, 15, self.volumen, "Grey", "White")

        
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self.btn_music)
        self.lista_widgets.append(self.picture_box)
        self.lista_widgets.append(self.btn_sound)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)

        self.render()


    def render(self):
        self._slave.fill(self._color_background)

    def btn_home_click(self, param):

        self.end_dialog()
    
    def update(self, lista_eventos):
        if self.active:
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
            self.render()
            self.update_volumen(lista_eventos)

    def btn_music_click(self, lista):
        print(self.bandera_musica)
        if self.bandera_musica:
            pygame.mixer.music.pause()
            self.btn_music._slave = self.off
        else:
            pygame.mixer.music.unpause()
            self.btn_music._slave = self.on

        self.bandera_musica = not self.bandera_musica

    def btn_sound_click(self, lista):
        if self.bandera_sonido:
            aux_image = pygame.image.load(lista[0])
            aux_image = pygame.transform.scale(aux_image,(60,60))
            self.btn_sound._slave = aux_image
        else:
            aux_image = pygame.image.load(lista[1])
            aux_image = pygame.transform.scale(aux_image,(60,60))
            self.btn_sound._slave = aux_image
        
        self.bandera_sonido = not self.bandera_sonido

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

# class FormSettings(Form):
#     def __init__(self, screen, x, y, w, h, color_background, color_border, border_size, active, path_image, volumen):
#         super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
#         self.volumen = volumen
#         self.flag_play = True 
#         self.off = "Recursos/items/music_off.png"
#         self.on = "Recursos/items/music_on.png"

#         self.picture_box = PictureBox(self._slave, 150, 30, 200, 80, path_image = "Recursos/modelo/logo.png")
#         self.btn_music =Button_Image(self._slave, x, y, 80, 140, 60, 60, path_image="Recursos/items/music_on.png", onclick= self.btn_music_click, onclick_param=["Recursos/items/music_off.png","Recursos/items/music_on.png"])
#         self.btn_sound =Button_Image(self._slave, x, y, 220, 140, 60, 60, path_image="Recursos/items/2.png", onclick= self.btn_sound_click, onclick_param=["Recursos/items/1.png","Recursos/items/2.png"])
#         self.label_volumen =Label(self._slave, 340, 140, 80, 50, "20%", font = "Comic Sans", font_size = 15, font_color = "Black", path_image = "Recursos/items/Gray.png")
#         self.slider_volumen = Slider(self._slave, x, y, 125, 260, 250, 15, self.volumen, "Grey", "White")

#         self._btn_home = Button_Image(screen=self._slave, x=400, y = 400, master_x=x, master_y=y,w =50,h=50,onclick=self.btn_home_click,onclick_param="",path_image="API_FORMS/home.png")

#         self.lista_widgets.append(self.picture_box)
#         self.lista_widgets.append(self._btn_home)
#         self.lista_widgets.append(self.btn_music)
#         self.lista_widgets.append(self.btn_sound)
#         self.lista_widgets.append(self.label_volumen)
#         self.lista_widgets.append(self.slider_volumen)

#         self.render()

# # 11:19 del video

#     def render(self):
#         self._slave.fill(self._color_background)


#     def btn_home_click(self, param):
#         self.end_dialog()
    
#     def update(self, lista_eventos):
#         if self.active:
#             self.draw()
#             for widget in self.lista_widgets:
#                 widget.update(lista_eventos)
#             self.update_volumen(lista_eventos)

#     def btn_music_click(self, lista):
#         if self.flag_play:
#             print("off")
#             pygame.mixer.music.pause()
#             aux_image = pygame.image.load(self.off)
#             aux_image = pygame.transform.scale(aux_image,(60,60))
#             self.btn_music._slave = aux_image
#         else:
#             print("on")
#             pygame.mixer.music.unpause()
#             aux_image = pygame.image.load(self.on)
#             aux_image = pygame.transform.scale(aux_image,(60,60))
#             self.btn_music._slave = aux_image

#         self.flag_play = not self.flag_play

#     def btn_sound_click(self, lista):
#         global bandera
#         if self.flag_play:
#             bandera = "Hola"
#             aux_image = pygame.image.load(lista[0])
#             aux_image = pygame.transform.scale(aux_image,(60,60))
#             self.btn_sound._slave = aux_image
#         else:
#             bandera = "Chau"
#             aux_image = pygame.image.load(lista[1])
#             aux_image = pygame.transform.scale(aux_image,(60,60))
#             self.btn_sound._slave = aux_image

#         self.flag_play = not self.flag_play

#     def update_volumen(self, lista_eventos):
#         self.volumen = self.slider_volumen.value
#         self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
#         pygame.mixer.music.set_volume(self.volumen)




