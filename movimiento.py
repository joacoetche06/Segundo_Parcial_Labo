import pygame
from configuraciones import *
contador_pasos = 0
desplazamiento_y = 0
bandera = True


def obtener_rectangulos(principal: pygame.Rect):
    diccionario = {}
    diccionario['main'] = principal
    diccionario['bottom'] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)#hay que restarle los pixeles que tiene el alto
    diccionario['right'] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
    diccionario['left'] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario['top'] = pygame.Rect(principal.left, principal.top, principal.width, 6)

    return diccionario
