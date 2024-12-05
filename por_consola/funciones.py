from por_consola.fijoss import diccionario_valores

def comparar_cartas(carta1, carta2) -> int:
    """
    Compara dos cartas y determina cuál es mayor.
    
    Parámetros:
        carta1 (Carta): La primera carta a comparar.
        carta2 (Carta): La segunda carta a comparar.
    
    Retorna:
        int: 1 si la primera carta es mayor, 2 si la segunda carta es mayor, 0 si son iguales.
    """
    valor1 = diccionario_valores.get(carta1.numero, carta1.numero)
    valor2 = diccionario_valores.get(carta2.numero, carta2.numero)
    return 1 if valor1 > valor2 else 2 if valor1 < valor2 else 0

def calcular_envido(mano) -> int:
    """
    Calcula el valor del envido para una mano.
    
    Parámetros:
        mano (list[tuple[int, str]]): La mano del jugador, representada por una lista de tuplas (valor, palo).
    
    Retorna:
        int: El valor máximo del envido en la mano.
    """
    palos = {}
    for carta in mano:
        if carta[1] not in palos:
            palos[carta[1]] = []
        palos[carta[1]].append(carta[0])
    max_envido = 0
    for cartas in palos.values():
        if len(cartas) > 1:
            max_envido = max(max_envido, sum(sorted(cartas)[-2:]) + 20)
    return max_envido

def tiene_flor(mano) -> bool:
    """
    Determina si una mano tiene flor.
    
    Parámetros:
        mano (list[tuple[int, str]]): La mano del jugador, representada por una lista de tuplas (valor, palo).
    
    Retorna:
        bool: True si la mano tiene flor, False si no.
    """
    palos = {}
    for carta in mano:
        if carta[1] not in palos:
            palos[carta[1]] = 0
        palos[carta[1]] += 1
    return any(cantidad >= 3 for cantidad in palos.values())

def calcular_flor(mano) -> int:
    """
    Calcula el valor de la flor para una mano.
    
    Parámetros:
        mano (list[tuple[int, str]]): La mano del jugador, representada por una lista de tuplas (valor, palo).
    
    Retorna:
        int: El valor de la flor si la mano tiene flor, 0 si no.
    """
    palos = {}
    for carta in mano:
        if carta[1] not in palos:
            palos[carta[1]] = []
        palos[carta[1]].append(carta[0])
    for cartas in palos.values():
        if len(cartas) >= 3:
            return sum(cartas[:3]) + 20
    return 0

def calcular_puntos_truco(nivel_truco) -> int:
    """
    Calcula los puntos que se otorgan por el nivel del truco.
    
    Parámetros:
        nivel_truco (str): El nivel del truco (por ejemplo, "Truco", "Retruco", "Vale Cuatro").
    
    Retorna:
        int: Los puntos correspondientes al nivel del truco.
    """
    if nivel_truco == "Truco":
        return 2
    elif nivel_truco == "Retruco":
        return 3
    elif nivel_truco == "Vale Cuatro":
        return 4
    return 1

def determinar_ganador_ronda(ganadores) -> int:
    """
    Determina el ganador de una ronda basada en los turnos ganados.
    
    Parámetros:
        ganadores (list[int]): Lista de los resultados de los turnos (1 si el primer jugador gana, 2 si el segundo jugador gana, 0 si es empate).
    
    Retorna:
        int: 1 si el primer jugador gana la ronda, 2 si el segundo jugador gana la ronda, 0 si es empate.
    """
    contador = {1: 0, 2: 0, 0: 0}
    for ganador in ganadores:
        contador[ganador] += 1
    return 1 if contador[1] > contador[2] else 2 if contador[2] > contador[1] else 0

def ganador_truco(mano1, mano2) -> int:
    """
    Determina el ganador del truco comparando las manos de dos jugadores.
    
    Parámetros:
        mano1 (list[Carta]): La mano del primer jugador.
        mano2 (list[Carta]): La mano del segundo jugador.
    
    Retorna:
        int: 1 si el primer jugador gana, 2 si el segundo jugador gana, 0 si es empate.
    """
    resultados = []
    for carta1, carta2 in zip(mano1, mano2):
        resultados.append(comparar_cartas(carta1, carta2))
    return determinar_ganador_ronda(resultados)

