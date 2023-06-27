import pygame

# Inicializar pygame
pygame.init()

# Cargar la imagen en una superficie
image_surface = pygame.image.load("Recursos/fotos/quieto/2.png")

# Obtener el tamaño de la superficie (cantidad de píxeles)
ancho, alto = image_surface.get_size()

# Calcular la cantidad total de píxeles
cantidad_pixeles = ancho * alto

# Imprimir la cantidad de píxeles
print("La imagen de ancho tiene", ancho, "y de alto", alto)
