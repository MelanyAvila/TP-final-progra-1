import csv
import os

def empezar_historial() -> None:
    '''
    esta funcion crea un archivo para el historial (si no existe) y agrega la info
    no recibe ni retorna nada
    '''
    archivo = 'historial.csv'
    
    if not os.path.exists(archivo):
        with open(archivo, mode="a", newline='', encoding='utf-8') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow([
                'Jugador1',  # nombre para j1
                'Puntos1',   # puntos
                'Jugador2', 
                'Puntos2'  
            ])

def guardar_info_partida(jugador1: dict, jugador2: dict, archivo: str = "historial.csv") -> None:
    '''
    esta funcion guarda la información de una partida en un archivo csv.
    recibe los diccionarios de los jugadores y el nombre de un archivo.
    no retorna nada.
    '''
    with open(archivo, mode="a", newline="", encoding="utf-8") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow([
            jugador1["nombre"], 
            jugador1["puntos"],
            jugador2["nombre"],
            jugador2["puntos"]
        ])
