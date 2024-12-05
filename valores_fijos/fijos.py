import pygame

pygame.init()

# PANTALLA
ANCHO_VENTANA = 900
ALTO_VENTANA = 600

VENTANA = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

# CARTAS
PALOS = ('bastos', 'espadas', 'copas', 'oros')
NUMEROS = (1, 2, 3, 4, 5, 6, 7, 10, 11, 12)

diccionario_valores = { # de mayor a menor valor
    (1, 'espadas'): 13, 
    (1, 'bastos'): 12, 
    (7, 'espadas'): 11, 
    (7, 'oros'): 10, 
    (3, 'espadas'): 9, (3, 'bastos'): 9, (3, 'oros'): 9, (3, 'copas'): 9,
    (2, 'espadas'): 8, (2, 'bastos'): 8, (2, 'oros'): 8, (2, 'copas'): 8,
    (1, 'oros'): 7, (1, 'copas'): 7,
    (12, 'espadas'): 6, (12, 'bastos'): 6, (12, 'oros'): 6, (12, 'copas'): 6,
    (11, 'espadas'): 5, (11, 'bastos'): 5, (11, 'oros'): 5, (11, 'copas'): 5,
    (10, 'espadas'): 4, (10, 'bastos'): 4, (10, 'oros'): 4, (10, 'copas'): 4,
    (7, 'copas'): 3, (7, 'bastos'): 3,
    (6, 'espadas'): 2, (6, 'bastos'): 2, (8, 'oros'): 2, (6, 'copas'): 2,
    (5, 'espadas'): 1, (5, 'bastos'): 1, (5, 'oros'): 1, (5, 'copas'): 1,
    (4, 'espadas'): 0, (4, 'bastos'): 0, (4, 'oros'): 0, (4, 'copas'): 0
}


# COLORES
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
CELESTE = (153, 203, 255)
VERDE = (0, 255, 0)

# FUENTES Y TAMAÑOS
fuentes = [
    pygame.font.SysFont("Times New Roman", 40), # 0
    pygame.font.SysFont('Times New Roman', 20),
    pygame.font.SysFont('Times New Roman', 15),
    pygame.font.SysFont('Times New Roman', 20, bold=True)
]

# FONDOS
FONDO = pygame.image.load('imagenes\\fondo\\fondo_inicio.jpg')
FONDO_JUEGO = pygame.image.load('imagenes\\fondo\\fondo.jpg')
FONDO_JUEGO = pygame.transform.scale(FONDO_JUEGO, (ANCHO_VENTANA, ALTO_VENTANA))
