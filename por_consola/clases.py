import random
from por_consola.fijoss import LISTA_PALOS, LISTA_NUMEROS, diccionario_valores

class Carta():
    valores = diccionario_valores
    def __init__(self, numero, palo) -> None:
        self.numero = numero
        self.palo = palo
       

        if (self.numero, self.palo) in self.valores:
            self.jerarquia = self.valores[(self.numero, self.palo)]
        else:  
            self.jerarquia = self.valores.get(self.numero)

    def mostrar(self):
        mensaje = f'{self.numero} de {self.palo}'
        return mensaje


class Mazo():
    def __init__(self):
        self.cartas = []
        for palo in LISTA_PALOS:
            for valor in LISTA_NUMEROS:
                carta = Carta(valor, palo)
                self.cartas.append(carta)
        random.shuffle(self.cartas)

    def agarrar(self):
        return self.cartas.pop()


class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        self.mano = []
        self.primera = False

    def agarrar_carta(self, carta):
        self.mano.append(carta)
    
    def mostrar_mano(self):
        if not self.mano:
            print('nada más') 
        else:
            print(f'mano de {self.nombre}')
            for i, carta in enumerate(self.mano, 1):
                print(f'{i})- {carta.mostrar()}')    

    def jugar_carta(self):
        self.mostrar_mano()
        opcion = int(input('qué carta quieres jugar?: '))
        self.carta_jugada = self.mano.pop(opcion - 1)

    def __str__(self):
        return self.nombre 
