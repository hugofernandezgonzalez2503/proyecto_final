# Importamos la biblioteca pyxel
import pyxel
# Importamos la clase Chef para poder utilizarla en la clase Tablero
from chef import Chef


class Tablero:
    def __init__(self, ancho:int, alto:int):
        self.ancho=ancho
        self.alto=alto
        self.chef1=Chef(self.ancho//2, 64, 0, 0, False)
        self.chef2=Chef(self.ancho//2, 128, 0, 0, False)

        pyxel.init(self.ancho, self.alto, title="Juego cocina", display_scale=4)
        pyxel.load("assets/resources.pyxres")
        pyxel.run(self.update, self.draw)

    @property
    def ancho(self)->int:
        return self.__ancho
    @ancho.setter
    def ancho(self, ancho:int):
        if not isinstance(ancho, int):
            raise TypeError("El ancho tiene que ser un entero")
        if ancho<1:
            raise ValueError("El ancho tiene que ser mayor que 0")
        self.__ancho=ancho

    @property
    def alto(self)->int:
        return self.__alto
    @alto.setter
    def alto(self, alto: int):
        if not isinstance(alto, int):
            raise TypeError("El alto tiene que ser un entero")
        if alto<1:
            raise ValueError("El alto tiene que ser positivo")
        self.__alto=alto

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(90, 98, 0, 0, 128, 12, 9, None, 0, scale=17.45)
        pyxel.blt(self.chef1.x, self.chef1.y, *self.chef1.imagen)
        pyxel.blt(self.chef2.x, self.chef2.y, *self.chef2.imagen)