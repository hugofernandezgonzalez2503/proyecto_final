import pyxel

class Chef:
    def __init__(self, x:int, y:int, imagen_x:int, imagen_y:int, plato:bool):
        """self.x indica la posicion x del chef en el tablero
        self.y indica la posicion y del chef en el tablero
        imagen_x e imagen_y son las coordenadas para elegir la imagen que queremos usar de resources"""
        self.x=x
        self.y=y
        self.imagen_x=imagen_x
        self.imagen_y=imagen_y
        self.plato=plato