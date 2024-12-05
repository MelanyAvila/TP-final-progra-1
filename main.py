from valores_fijos.fijos import *
from valores_fijos.ventanas import menu_inicio
from funciones.jugar import *
from funciones.jugador import crear_jugador
from funciones.historial import *
import pygame

pygame.init()

correr = True

mostrar_inicio = True

while correr == True:

    if mostrar_inicio == True:
        menu_inicio()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                correr = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if JUGAR_RECT.collidepoint(event.pos):
                    mostrar_inicio = False
                if SALIR_RECT.collidepoint(event.pos):
                    correr = False          
    else:
        jugador_1 = crear_jugador('')
        jugador_2 = crear_jugador('lacompu')
        puntos_ronda = 15
        ronda = 1
        mano = 1

        while jugador_1['puntos'] < puntos_ronda and jugador_2['puntos'] < puntos_ronda: 
            jugar_ronda(ronda, jugador_1, jugador_2, mano, puntos_ronda)
            ronda += 1
        guardar_info_partida(jugador_1, jugador_2)

        pygame.display.update() 

pygame.quit()