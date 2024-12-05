from valores_fijos.fijos import *

CANTAR_ENVIDO = fuentes[3].render('¡La maquina canta Envido!', True, NEGRO)
CANTAR_ENVIDO_RECT = pygame.Rect((350, 60), (45, 45)) 

CANTAR_REAL_ENVIDO = fuentes[3].render('¡La maquina canta Real Envido!', True, NEGRO)
CANTAR_REAL_ENVIDO_RECT = pygame.Rect((310, 60), (45, 45)) 

CANTAR_FALTA_ENVIDO = fuentes[3].render('¡La maquina canta Falta Envido!', True, NEGRO)
CANTAR_FALTA_ENVIDO_RECT = pygame.Rect((310, 60), (45, 45)) 

PERDER_ENVIDO = fuentes[3].render('¡Perdiste el envido!', True, ROJO)
PERDER_ENVIDO_RECT = pygame.Rect((375, 60), (45, 45)) 

GANAR_ENVIDO = fuentes[3].render('¡Ganaste el envido!', True, VERDE)
GANAR_ENVIDO_RECT = pygame.Rect((375, 60), (45, 45)) 

CANTAR_TRUCO = fuentes[3].render('¡La maquina canta Truco!', True, NEGRO)
CANTAR_TRUCO_RECT = pygame.Rect((350, 60), (45, 45)) 

CANTAR_RE_TRUCO = fuentes[3].render('¡La maquina canta Re Truco!', True, NEGRO)
CANTAR_RE_TRUCO_RECT = pygame.Rect((320, 60), (45, 45)) 

CANTAR_VALE_CUATRO = fuentes[3].render('¡La maquina canta Vale Cuatro!', True, NEGRO)
CANTAR_VALE_CUATRO_RECT = pygame.Rect((310, 60), (45, 45)) 

PERDER_TRUCO = fuentes[3].render('¡Perdiste el truco!', True, ROJO)
PERDER_TRUCO_RECT = pygame.Rect((375, 60), (45, 45)) 

GANAR_TRUCO = fuentes[3].render('¡Ganaste el truco!', True, VERDE)
GANAR_TRUCO_RECT = pygame.Rect((375, 60), (45, 45)) 

EMPATE = fuentes[3].render('¡EMPATE!', True, NEGRO)
EMPATE_RECT = pygame.Rect((400, 60), (45, 45)) 

GANAR_MANO = fuentes[1].render('¡Ganaste la mano!...', True, ROJO)
GANAR_MANO_RECT = pygame.Rect((400, 100), (90, 45))

PERDER_MANO = fuentes[1].render('¡Perdiste la mano!...', True, ROJO)
PERDER_MANO_RECT = pygame.Rect((400, 100), (90, 45))