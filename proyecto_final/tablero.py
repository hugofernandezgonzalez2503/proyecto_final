import pyxel

from chef import Chef

class Tablero:
    def __init__(self, ancho:int, alto:int):
        self.ancho=ancho
        self.alto=alto
        self.chef1=Chef(self.ancho//2, self.alto//4)
        self.chef2=Chef(self.ancho//2, 3*self.alto//4)