from por_consola.clases import Mazo, Jugador
from por_consola.funciones import *
import random

# acá esta lo primero que presente! no toque o cambie nada porque me centre directamete en pygame

mazo = Mazo()

nombre_jugador = input("Ingresa tu nombre: ")                     
jugador1 = Jugador(nombre_jugador)
jugador2 = Jugador('lacompu')  

correr = True

while correr:
    print(f'{jugador1} tiene {jugador1.puntos} puntos')
    print(f'{jugador2} tiene {jugador2.puntos} puntos')

    jugador1.mano = []
    jugador2.mano = []

    for _ in range(3):
        jugador1.agarrar_carta(mazo.agarrar())
        jugador2.agarrar_carta(mazo.agarrar())

    ganador = False
    ronda = 1
    jugador1.primera = False
    jugador2.primera = False

    envido_jugador1 = calcular_envido([(carta.numero, carta.palo) for carta in jugador1.mano])
    envido_jugador2 = calcular_envido([(carta.numero, carta.palo) for carta in jugador2.mano])

    while ronda <= 3 and not ganador:
        print(f'\n--- Ronda {ronda} ---')
        print('Tus cartas:')
        jugador1.mostrar_mano()

        opcion = input('Elige una carta (número) o canta (envido/truco/flor): ').lower()

        match opcion:
            case 'envido':
                if ronda == 1:
                    print(f'Envido de {jugador1}: {envido_jugador1}')
                    print(f'Envido de {jugador2}: {envido_jugador2}')
                    if envido_jugador1 > envido_jugador2:
                        print(f'{jugador1.nombre} gana el Envido')
                        ronda -= 1
                        jugador1.puntos += 2
                    elif envido_jugador2 > envido_jugador1:
                        print(f'{jugador2.nombre} gana el Envido')
                        ronda -= 1
                        jugador2.puntos += 2
                    else:
                        print('Empate en el Envido')
                else:
                    print('Solo se puede calcular envido en la primera ronda')
                    ronda -= 1
            case 'flor':
                tiene_flor_j1 = tiene_flor([(carta.numero, carta.palo) for carta in jugador1.mano])
                tiene_flor_j2 = tiene_flor([(carta.numero, carta.palo) for carta in jugador2.mano])
                if tiene_flor_j1:
                    flor_j1 = calcular_flor([(carta.numero, carta.palo) for carta in jugador1.mano])
                    print(f'{jugador1.nombre} tiene Flor: {flor_j1}')
                    jugador1.puntos += 3
                    ronda -= 1
                if tiene_flor_j2:
                    flor_j2 = calcular_flor([(carta.numero, carta.palo) for carta in jugador2.mano])
                    print(f'{jugador2.nombre} tiene Flor: {flor_j2}')
                    jugador2.puntos += 3
                    ronda -= 1
                if not tiene_flor_j1 and not tiene_flor_j2:
                    print('Ningún jugador tiene Flor.')
                    ronda -= 1
            case 'truco':
                nivel_truco = input('Nivel del Truco (Truco/Retruco/Vale Cuatro): ').capitalize()
                ganador_truco_actual = ganador_truco(jugador1.mano, jugador2.mano)
                puntos_truco = calcular_puntos_truco(nivel_truco)
                print(f'Ganador del Truco: {jugador1.nombre if ganador_truco_actual == 1 else jugador2.nombre if ganador_truco_actual == 2 else 'Empate'}')
                if ganador_truco_actual == 1:
                    jugador1.puntos += puntos_truco
                elif ganador_truco_actual == 2:
                    jugador2.puntos += puntos_truco
                ronda -= 1
            case _: 
                    if opcion.isdigit():  
                        try: # cambiar
                            indice = int(opcion) - 1
                            jugador1.carta_jugada = jugador1.mano.pop(indice)
                            print(f'{jugador1.nombre} jugó: {jugador1.carta_jugada.mostrar()}')

                            jugador2.carta_jugada = random.choice(jugador2.mano)
                            jugador2.mano.remove(jugador2.carta_jugada)
                            print(f'{jugador2.nombre} jugó: {jugador2.carta_jugada.mostrar()}')

                            # Comparar cartas
                            if jugador1.carta_jugada.jerarquia > jugador2.carta_jugada.jerarquia:
                                print(f'{jugador1.nombre} gana el turno')
                                if jugador1.primera:
                                    print(f'¡{jugador1.nombre} ganó la mano!')
                                    jugador1.puntos += 1
                                    ganador = True
                                else:
                                    jugador1.primera = True
                            elif jugador1.carta_jugada.jerarquia < jugador2.carta_jugada.jerarquia:
                                print(f'{jugador2.nombre} gana el turno')
                                if jugador2.primera:
                                    print(f'¡{jugador2.nombre} ganó la mano!')
                                    jugador2.puntos += 1
                                    ganador = True
                                else:
                                    jugador2.primera = True
                            else:
                                print('Empate')
                        except (ValueError, IndexError):
                            print('Número inválido, elige una opción válida.')
                    else:
                        print('Opción inválida, intenta nuevamente.')       
        ronda += 1

        if jugador1.puntos >= 30:
            print(f'¡{jugador1.nombre} gana el truco con {jugador1.puntos} puntos!')
            correr = False
            break
        elif jugador2.puntos >= 30:
            print(f'¡{jugador2.nombre} gana el truco con {jugador2.puntos} puntos!')
            correr = False
            break