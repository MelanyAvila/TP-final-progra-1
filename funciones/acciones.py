import random
import pygame
from valores_fijos.fijos import *

def generar_mazo(palos: tuple, numeros: tuple, valores: dict) -> list:
    '''
    esta funcion genera un mazo de cartas como una lista de diccionarios.
    recibe como parametros tuplas con los nombres de los palos y los numeros de las cartas,
    diccionario con los valores de las cartas.
    retorna una lista de diccionarios, cada uno representando una carta y sus especificaciones.
    '''
    mazo = [] 
    for palo in palos:
        for numero in numeros:
            valor = valores.get((numero, palo), valores.get(numero, numero))

            ruta_completa = f'imagenes\\cartas\\{numero}_{palo}.jpg'
            
            carta = {
                'numero': numero,
                'palo': palo,
                'valor': valor,
                'imagen': pygame.image.load(ruta_completa)
            }

            mazo.append(carta)

    return mazo

def repartir_cartas(mazo: dict) -> tuple:
    '''
    esta funcion reparte 3 cartas (unicas) para dos jugadores, sin repetir las cartas de cada uno.
    recibe como parametro un diccionario con todas las cartas.
    retorna una tupla con dos listas que representan las cartas de cada jugador 
    '''
    mano_jugador_1 = []
    mano_jugador_2 = []

    while len(mano_jugador_1) < 3: 
        carta = random.choice(mazo) 
        if carta not in mano_jugador_1: 
            mano_jugador_1.append(carta) 
        carta = random.choice(mazo)
        if carta not in mano_jugador_1 and carta not in mano_jugador_2:
            mano_jugador_2.append(carta)
    return mano_jugador_1, mano_jugador_2

def valores_envido(numero: int) -> int:
    '''
    esta funcion verifica cuanto vale el envido (0 para las figuras y el resto vale lo mismo).
    recibe el numero de carta y retorna el valor.
    '''
    if numero == 10 or numero == 11 or numero == 12:  
        return 0
    else:
        return numero  

def calcular_envido(cartas_dadas: list) -> int:
    ''' 
    calcula cuántos puntos tiene de envido a partir de las cartas de una mano.
    recibe como parámetro una lista con las 3 cartas y retorna el total de los puntos.
    '''
    
    cartas = len(cartas_dadas)
    # bucle para ordenar las cartas en cartas_dadas por su valor de envido en orden.
    # compara el valor de envido de dos cartas y si el valor de envido de cartas_dadas[j] es menor que cartas_dadas[j + 1], se intercambian las posiciones.
    for i in range(cartas):
        for j in range(cartas - i - 1):
            if valores_envido(cartas_dadas[j]['numero']) < valores_envido(cartas_dadas[j + 1]['numero']):
                cartas_dadas[j], cartas_dadas[j + 1] = cartas_dadas[j + 1], cartas_dadas[j]

    # combinaciones posibles de pares de cartas
    posibles = []
    for i in range(cartas):
        for j in range(i + 1, cartas):
            posibles.append((cartas_dadas[i], cartas_dadas[j]))

    total_puntos = 0

    for carta1, carta2 in posibles: # itera sobre cada combinación posible de pares
        if carta1['palo'] == carta2['palo']:  # solo suman si son del mismo palo
            puntos = valores_envido(carta1['numero']) + valores_envido(carta2['numero']) + 20
            total_puntos = max(total_puntos, puntos) # se actualiza con el valor máximo entre total_puntos actual y puntos

    # si no hay envido, devolver el valor de la mejor carta
    if total_puntos == 0:
        return valores_envido(cartas_dadas[0]['numero'])

    return total_puntos
 
def verificar_envido(jugador_1: dict, jugador_2: dict, tipo: str, envido_jugador_1: int, envido_jugador_2: int, mano: int, puntos_maximos: int = 33) -> tuple:
    '''
    esta funcion determina el ganador de una ronda de envido, actualiza los puntos del ganador y 
    retorna el estado actualizado de ambos jugadores junto con el ganador del envido.
    recme como parametros dos dicionarios (jugadores), tipo de envido para calcularlo, los puntos del envido
    de cada jugador,  la mano, y los puntos maximos del envido (33).
    '''
    # ganador
    if envido_jugador_1 > envido_jugador_2:
        ganador_envido = jugador_1
    elif envido_jugador_1 < envido_jugador_2:
        ganador_envido =  jugador_2
    else:  # empate
        if mano == 1:
            ganador_envido = jugador_1
        elif mano == -1:
            ganador_envido = jugador_2

    if jugador_1['puntos'] > jugador_2['puntos']:
        subir_puntos = jugador_1['puntos']
    elif jugador_1['puntos'] < jugador_2['puntos']:
        subir_puntos = jugador_2['puntos']
    else:
        subir_puntos = jugador_1['puntos']

    if tipo == 'envido':
        puntos = 2
    elif tipo == 'real envido':
        puntos = 3
    elif tipo == 'falta envido':
        puntos = puntos_maximos - subir_puntos    

    # actualizar
    if ganador_envido == 'jugador':
        jugador_1['puntos'] += puntos
    else:  # ganador_envido == 'jugador2'
        jugador_2['puntos'] += puntos

    return ganador_envido, jugador_1, jugador_2

def definir_mano(carta_jugador_1: dict, carta_jugador_2: dict, rondas_ganadas_jugador_1: int, rondas_ganadas_jugador_2: int, mano: int, valores: dict):
    '''
    esta funcion determina el ganador definitivo de una mano, actualiza el número de rondas ganadas por cada jugador,
    retorna el ganador de la mano y las rondas ganadas por cada jugador.
    recibe como parametros dos diccionarios con la ifo de cada carta, el numero de rondas ganadas de cada jugador, 
    la mano y los valores de las cartas
    '''
    # valor de la carta de j1
    numero_jugador_1 = carta_jugador_1.get('numero')
    palo_jugador_1 = carta_jugador_1.get('palo')
    valor_jugador_1 = valores.get((numero_jugador_1, palo_jugador_1), valores.get(numero_jugador_1, 0))
    
    # valor de la carta de j2
    numero_jugador_2 = carta_jugador_2.get('numero')
    palo_jugador_2 = carta_jugador_2.get('palo')
    valor_jugador_2 = valores.get((numero_jugador_2, palo_jugador_2), valores.get(numero_jugador_2, 0))
    
    # ganador de la mano actual
    if valor_jugador_1 > valor_jugador_2:
        ganador = 1
        rondas_ganadas_jugador_1 += 1
    elif valor_jugador_2 > valor_jugador_1:
        ganador = -1
        rondas_ganadas_jugador_2 += 1
    else:
        # empate
        ganador = 0
    
    # reglas adicionales para el ganador definitivo
    if rondas_ganadas_jugador_1 == 2:
        ganador = 1
    elif rondas_ganadas_jugador_2 == 2:
        ganador = -1
    elif rondas_ganadas_jugador_1 == 1 and rondas_ganadas_jugador_2 == 1:
        ganador = mano
    elif ganador == 0 and rondas_ganadas_jugador_1 + rondas_ganadas_jugador_2 == 0:
        # si todos empataron, define al ganador como la mano
        ganador = mano
    
    return ganador, rondas_ganadas_jugador_1, rondas_ganadas_jugador_2

def verificar_puntos(ganador_mano: int, tipo: str, jugador_1: dict, jugador_2: dict) -> tuple:
    '''
    esta funcion actualiza los puntos de los jugadores según el ganador de la mano y el tipo de truco jugado,
    recibe como parametros el ganador de la mano, el tipo de truco jugado, y los diccionadios de los ugadores (para los puntos)
    retorna los puntos actualizados.
    '''
    if tipo == 'truco':
        puntos = 2
    elif tipo == 're truco':
        puntos = 3
    elif tipo == 'vale cuatro':
        puntos = 4
    else:
        puntos = 1

    if ganador_mano == 1:
        jugador_1['puntos'] += puntos
    else:
        jugador_2['puntos'] += puntos

    return jugador_1['puntos'], jugador_2['puntos']