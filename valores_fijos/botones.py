from valores_fijos.fijos import *

JUGAR_BOTON = fuentes[0].render('JUGAR', True, VERDE)
JUGAR_RECT = pygame.Rect((225, 400), (90, 45)) 

SALIR_BOTON = fuentes[0].render('SALIR', True, ROJO)
SALIR_RECT = pygame.Rect((550, 400), (90, 45))

# JUEGO
ENVIDO_BOTON = fuentes[1].render('ENVIDO', True, NEGRO)
ENVIDO_RECT = pygame.Rect((775, 525),(100, 40))

REAL_ENVIDO_BOTON = fuentes[1].render('REAL ENVIDO', True, NEGRO)
REAL_ENVIDO_RECT = pygame.Rect((720, 475), (155, 40))

FALTA_ENVIDO_BOTON = fuentes[1].render('FALTA ENVIDO', True, NEGRO)
FALTA_ENVIDO_RECT = pygame.Rect((715, 425), (160, 40))

TRUCO_BOTON = fuentes[1].render('TRUCO', True, NEGRO)
TRUCO_RECT = pygame.Rect((25, 525), (90, 40))

RE_TRUCO_BOTON = fuentes[1].render('RE TRUCO', True, NEGRO)
RE_TRUCO_RECT = pygame.Rect((25, 475), (115, 40))

VALE_CUATRO_BOTON = fuentes[1].render('VALE CUATRO', True, NEGRO)
VALE_CUATRO_RECT = pygame.Rect((25, 425), (155, 40))

ACEPTAR_BOTON = fuentes[1].render('\"QUIERO\"', True, VERDE)
ACEPTAR_RECT = pygame.Rect((60, 380), (100, 40))

RECHAZAR_BOTON = fuentes[1].render('\"NO QUIERO\"', True, ROJO)
RECHAZAR_RECT = pygame.Rect((735, 380), (100, 40))

botones = [
    (ENVIDO_BOTON, ENVIDO_RECT),
    (REAL_ENVIDO_BOTON, REAL_ENVIDO_RECT),
    (FALTA_ENVIDO_BOTON, FALTA_ENVIDO_RECT),
    (ACEPTAR_BOTON, ACEPTAR_RECT),
    (RECHAZAR_BOTON, RECHAZAR_RECT),
    (TRUCO_BOTON, TRUCO_RECT),
    (RE_TRUCO_BOTON, RE_TRUCO_RECT),
    (VALE_CUATRO_BOTON, VALE_CUATRO_RECT),
]