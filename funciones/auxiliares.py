import pygame
from valores_fijos.fijos import *

def cargar_imagen(imagen: pygame.Surface, posicion: tuple) -> tuple:
    '''
    esta funcion  ajusta la posicion de una imagen en pygame.
    recibe coomo parametros la magen a posicionar y la posicion x, y
    retorna tanto la imagen como el rectangulo
    '''
    rect = imagen.get_rect()
    rect.topleft = posicion
    return imagen, rect

def render_turno(turno: int) -> list: # mejorar, usar paradigmas funcionales para las fuentes, posicionamiento y color
    '''
    esta funcion crea una representación grafica que indica el turno actual,
    renderiza el texto usando una fuente y calcula el rectángulo de posicionamiento 
    '''
    TURNOS = fuentes[3].render(f'¡Turno {turno}!', True, NEGRO)
    TURNOS_RECT = pygame.Rect((10, 10), (45, 45)) 
    texto_turno = [TURNOS, TURNOS_RECT]
    return texto_turno

def render_puntos(jugador: dict, color: tuple, x: int, y: int) -> tuple:
    '''
    esta funcion crea una representacion grafica de un jugador, renderiza 
    el texto con una fuente y calcula el rect de posicionamiento.
    recibe como parametros: el jugador (dict con la info de los puntos), un color rgb,
    y las posiciones X e Y
    '''
    texto = f'puntos de {jugador['nombre']}: {jugador['puntos']}'

    PUNTOS = fuentes[1].render(texto, True, color)

    PUNTOS_RECT = PUNTOS.get_rect(center=(x, y))

    return PUNTOS, PUNTOS_RECT

def mostrar_botones(ventana: pygame.Surface, botones: list, color: tuple) -> None:
    '''
    esta funcion dibuja botones con texto en una superficie.
    recibe un objeto de tipo pygame.Surface para que reciba cualquier superficie sobre la que se quiera dibujar,
    una lista de tuplas que contiene: boton y rect (posición y tamaño) y una tupla RGB para el color del botón.
    '''
    for boton, rect in botones:
        pygame.draw.rect(ventana, color, rect, border_radius=20)
        ventana.blit(boton, (rect.x + 10, rect.y + 5))