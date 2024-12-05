def crear_jugador(nombre: str) -> dict:
    '''
    crea un jugador con un nombre y puntos iniciales.
    recibe el nombre y retorna un diccionario con los datos
    '''
    jugador = {
        'nombre': nombre,
        'puntos': 0,
        'cartas':[],
        'tantos': []
    }
    return jugador