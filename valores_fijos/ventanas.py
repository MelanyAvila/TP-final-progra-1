from valores_fijos.fijos import *
from valores_fijos.textos import *
from valores_fijos.botones import *
import pygame

def menu_inicio() -> None:
    '''
    configura y muestra la pantalla de inicio. establece el título de la ventana, 
    dibuja el fondo, y muestra los botones de jugar y salir.
    no recibe ni retorna nada.
    '''
    pygame.display.set_caption('\"Menu\"')
    
    VENTANA.blit(FONDO,(0,0))

    VENTANA.blit(JUGAR_BOTON, JUGAR_RECT)
    VENTANA.blit(SALIR_BOTON, SALIR_RECT)
    
    pygame.display.update()


def terminar_mano(jugador_1: dict, jugador_2: dict, triunfo_j1: bool, triunfo_j2: bool, ganador_mano=None) -> tuple:
    '''
    esta funcion festiona la visualizacion en pygame del resultado de una mano, muestra un mensaje.
    recibe como parametros los jugadores (diccionarios con la info de cada uno), dos booleanos para indicar quien gano 
    y el ganador de la mano. retorna una tupla con los puntos de cada jugador.
    '''
    pygame.init()

    run_game = True

    while run_game: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        VENTANA.fill(NEGRO)  

        if triunfo_j1:
            VENTANA.blit(GANAR_MANO, GANAR_MANO_RECT)  
        elif triunfo_j2:
            VENTANA.blit(PERDER_MANO, PERDER_MANO_RECT)
        elif ganador_mano == 1:
            VENTANA.blit(GANAR_MANO, GANAR_MANO_RECT)
        elif ganador_mano == -1:
            VENTANA.blit(PERDER_MANO, PERDER_MANO_RECT)
              
        pygame.display.update()

    pygame.quit()

    return (jugador_1['puntos'], jugador_2['puntos'])
