import pygame
import random
from valores_fijos.fijos import *
from valores_fijos.ventanas import *
from valores_fijos.botones import *
from valores_fijos.textos import *
from funciones.acciones import *
from funciones.auxiliares import *

pygame.init()

def jugar_ronda(rondas: int, jugador_1: dict, jugador_2: dict, mano: int, puntos_maximos: int):

    # JUGADOR 1: usuario, # JUGADOR 2: la compu

    mazo_cartas = generar_mazo(PALOS, NUMEROS, diccionario_valores)

    cartas_jugador_1, cartas_jugador_2 = repartir_cartas(mazo_cartas) 


    jugador_1['cartas'] = cartas_jugador_1
    jugador_2['cartas'] = cartas_jugador_2

    tantos_jugador_1 = calcular_envido(cartas_jugador_1)
    tantos_jugador_2 = calcular_envido(cartas_jugador_2)

    jugador_1['tantos'] = tantos_jugador_1
    jugador_2['tantos'] = tantos_jugador_2

    while calcular_envido(cartas_jugador_2) < 20:
        cartas_jugador_1, cartas_jugador_2 = repartir_cartas(mazo_cartas)

    # variables
    turnos = 0 
    carta_jugador_1 = None
    carta_jugador_2 = None
    horizontal_x = 0
    vueltas = 0
    cartas_elegidas_jugador_2 = []
    vueltas_ganadas_jugador_2 = 0
    vueltas_ganadas_jugador_1 = 0
    empates = 0
    tipo_punto = None
    ganador_envido = None

    # banderas
    vale_cuatro_cantado = False
    j2_canto_envido = False
    re_truco_cantado = False
    envido_cantado = False 
    truco_cantado =  False 
    turno = -1 
    j2_ya_jugo = False 
    j1_ya_jugo = False 
    carta_j2_elegida = False 

    # imagenes de las cartas
    carta_1_elegida = False
    carta_2_elegida = False
    carta_3_elegida = False
    mostrar_j2_1 = False
    mostrar_j2_2 = False
    mostrar_j2_3 = False

    # cargar las imagenes
    carta_1, imagen_rect_carta_1 = cargar_imagen(cartas_jugador_1[0]['imagen'], (260, 410))  
    carta_2, imagen_rect_carta_2 = cargar_imagen(cartas_jugador_1[1]['imagen'], (380, 410))
    carta_3, imagen_rect_carta_3 = cargar_imagen(cartas_jugador_1[2]['imagen'], (500, 410))

    carta_j2_1, imagen_rect_carta_j2_1 = cargar_imagen(cartas_jugador_2[0]['imagen'], (260, 70))
    carta_j2_2, imagen_rect_carta_j2_2 = cargar_imagen(cartas_jugador_2[1]['imagen'], (380, 70))
    carta_j2_3, imagen_rect_carta_j2_3 = cargar_imagen(cartas_jugador_2[2]['imagen'], (500, 70))

    PUNTOS_JUGADOR_1, PUNTOS_JUGADOR_1_RECT = render_puntos(jugador_1, ROJO, 810, 20)
    PUNTOS_JUGADOR_2, PUNTOS_JUGADOR_2_RECT = render_puntos(jugador_2, ROJO, 80, 20)
  
    # INICIO DEL JUEGO
    correr = True

    texto_turno, rect_turno = render_turno(turno)
    VENTANA.blit(texto_turno, rect_turno.topleft) # para establecer las coordenadas del punto superior izquierdo del rectángulo

    while correr == True:
        # eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                correr = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if imagen_rect_carta_1.collidepoint(event.pos) and turno == 1 and carta_1_elegida == False:
                    carta_jugador_1 = cartas_jugador_1[0]  # selecciona correctamente la carta
                    j1_ya_jugo = True
                    imagen_rect_carta_1.center = (240 + horizontal_x, 220)
                    carta_1_elegida = True
                elif imagen_rect_carta_2.collidepoint(event.pos) and turno == 1 and carta_2_elegida == False:
                    carta_jugador_1 = cartas_jugador_1[1]
                    j1_ya_jugo = True
                    imagen_rect_carta_2.center = (240 + horizontal_x, 220)
                    carta_2_elegida = True
                elif imagen_rect_carta_3.collidepoint(event.pos) and turno == 1 and carta_3_elegida == False:
                    carta_jugador_1 = cartas_jugador_1[2]
                    j1_ya_jugo = True
                    imagen_rect_carta_3.center = (240 + horizontal_x, 220)
                    carta_3_elegida = True
                    
                if ENVIDO_RECT.collidepoint(event.pos) and rondas == 0 and (turno == 1 or turnos == 0):
                    ganador_envido, jugador_1, jugador_2 = verificar_envido(jugador_1, jugador_2, 'envido', tantos_jugador_1, tantos_jugador_2, mano)
                    envido_cantado = True
                elif REAL_ENVIDO_RECT.collidepoint(event.pos) and rondas == 0 and (turno == 1 or turnos == 0):
                    ganador_envido, jugador_1, jugador_2 = verificar_envido(jugador_1, jugador_2, 'real envido', tantos_jugador_1, tantos_jugador_2, mano)
                    envido_cantado = True
                elif FALTA_ENVIDO_RECT.collidepoint(event.pos) and rondas == 0 and (turnos == 1 or turnos == 0):
                    ganador_envido, jugador_1, jugador_2 = verificar_envido(jugador_1, jugador_2, 'falta envido', tantos_jugador_1, tantos_jugador_2, mano)
                    envido_cantado = True

                if ACEPTAR_RECT.collidepoint(event.pos) and (j2_canto_envido):
                    if turnos == 0 or turnos == 1:
                        if tantos_jugador_1 >= 30:
                            ganador_envido, jugador_1, jugador_2 = verificar_envido(
                                jugador_1, jugador_2, tantos_jugador_1, tantos_jugador_2, mano
                            )
                        else:
                            ganador_envido, jugador_1, jugador_2 = verificar_envido(jugador_1, jugador_2, 'envido', tantos_jugador_1, tantos_jugador_2, mano)
                    envido_cantado = True
                    j2_canto_envido = False  
                elif RECHAZAR_RECT.collidepoint(event.pos) and rondas == 0: 
                    if turnos == 0 or turnos == 1:
                        ganador_envido = jugador_2
                        jugador_2['puntos'] += 1
                        envido_cantado = True 
                            
                if TRUCO_RECT.collidepoint(event.pos) and turno == 1 and truco_cantado == False:
                    ganador_mano, jugador_1, jugador_2 = verificar_puntos(ganador_mano, 'truco', jugador_1, jugador_2)
                    truco_cantado = True
                elif RE_TRUCO_RECT.collidepoint(event.pos) and truco_cantado == True:
                    ganador_mano, jugador_1, jugador_2 = verificar_puntos(ganador_mano, 're truco', jugador_1, jugador_2)
                    re_truco_cantado = True
                elif VALE_CUATRO_RECT.collidepoint(event.pos) and re_truco_cantado == True:
                    ganador_mano, jugador_1, jugador_2 = verificar_puntos(ganador_mano, 'vale cuatro', jugador_1, jugador_2)
                    vale_cuatro_cantado = True
            
        # acá inicia el juego
        VENTANA.blit(FONDO_JUEGO,(0,0))

        if mano == -1:
            vueltas = 5
        else:
            vueltas = 6
        
        if turnos == 2 or turnos == 3:
            horizontal_x = 200
        elif turnos == 4 or turnos == 6:
            horizontal_x = 400
        
        # maquina canta envido
        if random.random() < 0.5:  #  probabilidad del 50%
            if turnos == 0 or turnos == 1:
                if turno == -1 and envido_cantado == False:
                    if tantos_jugador_1 > 30:
                        VENTANA.blit(CANTAR_FALTA_ENVIDO, CANTAR_FALTA_ENVIDO_RECT) 
                        j2_canto_envido = True  
                        envido_cantado = True
                    else:
                        VENTANA.blit(CANTAR_ENVIDO, CANTAR_ENVIDO_RECT)
                        j2_canto_envido = True  
                        envido_cantado = True

                    VENTANA.blit(ACEPTAR_BOTON, ACEPTAR_RECT)
                    VENTANA.blit(RECHAZAR_BOTON, RECHAZAR_RECT)

        # maquina elije carta
        if turnos < vueltas:
            if turno == -1 and envido_cantado and carta_j2_elegida == False:
                carta_jugador_2 = random.choice(cartas_jugador_2)
                while carta_jugador_2 in cartas_elegidas_jugador_2:
                    carta_jugador_2 = random.choice(cartas_jugador_2)
                cartas_elegidas_jugador_2.append(carta_jugador_2)
                j2_ya_jugo = True
                carta_j2_elegida = True
                        
        # mostrar cartas j2
        if turnos < vueltas:
            if carta_j2_elegida:
                carta_jugador_2 == cartas_jugador_2[0]
                imagen_rect_carta_j2_1.center = (240 + horizontal_x, 190)
                mostrar_j2_1 = True 
            elif carta_j2_elegida:
                carta_jugador_2 == cartas_jugador_2[1]
                imagen_rect_carta_j2_2.center = (240 + horizontal_x, 190)
                mostrar_j2_2 = True
            elif carta_j2_elegida:
                carta_jugador_2 == cartas_jugador_2[2]
                imagen_rect_carta_j2_3.center = (240 + horizontal_x, 190)
                mostrar_j2_3 = True

        #  dibujar
        VENTANA.blit(carta_1, imagen_rect_carta_1)
        VENTANA.blit(carta_2, imagen_rect_carta_2)
        VENTANA.blit(carta_3, imagen_rect_carta_3)             
                
        if mostrar_j2_1:
            VENTANA.blit(carta_j2_1, imagen_rect_carta_j2_1)
        if mostrar_j2_2:
            VENTANA.blit(carta_j2_2, imagen_rect_carta_j2_2)
        if mostrar_j2_3:
            VENTANA.blit(carta_j2_3, imagen_rect_carta_j2_3)    

        mostrar_botones(VENTANA, [(TRUCO_BOTON, TRUCO_RECT)] , CELESTE)  
        mostrar_botones(VENTANA, [(RE_TRUCO_BOTON, RE_TRUCO_RECT)] , CELESTE)  
        mostrar_botones(VENTANA, [(VALE_CUATRO_BOTON, VALE_CUATRO_RECT)] , CELESTE) 

        mostrar_botones(VENTANA, [(ENVIDO_BOTON, ENVIDO_RECT)] , CELESTE)  
        mostrar_botones(VENTANA, [(REAL_ENVIDO_BOTON, REAL_ENVIDO_RECT)] , CELESTE)  
        mostrar_botones(VENTANA, [(FALTA_ENVIDO_BOTON, FALTA_ENVIDO_RECT)] , CELESTE)

        VENTANA.blit(PUNTOS_JUGADOR_1, PUNTOS_JUGADOR_1_RECT)
        VENTANA.blit(PUNTOS_JUGADOR_2, PUNTOS_JUGADOR_2_RECT)

        if turnos == 0 or turnos == 1:
            if envido_cantado == True and ganador_envido is not None:
                if ganador_envido == jugador_1:
                    VENTANA.blit(GANAR_ENVIDO, GANAR_ENVIDO_RECT)
                elif ganador_envido == jugador_2:
                    VENTANA.blit(PERDER_ENVIDO, PERDER_ENVIDO_RECT)
                else:
                    VENTANA.blit(EMPATE, EMPATE_RECT)     

        # cambiar de turno
        if j1_ya_jugo == True and turno == 1:
            turno *= -1
            turnos += 1
            # turno de j2
        elif j2_ya_jugo == True and turno == -1:
            turno *= -1
            turnos += 1
        
        if j1_ya_jugo == True and j2_ya_jugo == True:
            ganador_mano, vueltas_ganadas_jugador_1, vueltas_ganadas_jugador_2 = definir_mano(carta_jugador_1, carta_jugador_2, vueltas_ganadas_jugador_1, vueltas_ganadas_jugador_2, mano, diccionario_valores)
            jugador_1, jugador_2 = verificar_puntos(ganador_mano, tipo_punto, jugador_1, jugador_2)
            
            if ganador_mano == jugador_1:
                if jugador_1['puntos'] >= puntos_maximos:
                    terminar_mano(jugador_1, jugador_2, True, False, ganador_mano)
                else:
                    terminar_mano(jugador_1, jugador_2, False, False, ganador_mano)
            elif ganador_mano == jugador_2:
                if jugador_2['puntos'] >= puntos_maximos:
                    terminar_mano(jugador_1, jugador_2, False, True, ganador_mano)
                else:
                    terminar_mano(jugador_1, jugador_2, False, False, ganador_mano)
                    
            j1_ya_jugo = False
            carta_jugador_1 = None
            j2_ya_jugo = False
            carta_jugador_2 = None
            carta_j2_elegida = False
        
        pygame.display.update()      

    pygame.quit()