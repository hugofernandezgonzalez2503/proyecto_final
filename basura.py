import pyxel
from plato import Plato


class CuboBasura:
    """Representa el cubo de basura compartido de la cocina.

    Permite a los chefs vaciar el contenido de un plato que lleven en la mano
    sin destruir el plato.
    """

    def __init__(self, x: int, y: int, u: int, v: int, tamano: int = 16):
        """Inicializa el cubo de basura con su posición y sprite.

        :param x: coordenada X en píxeles
        :param y: coordenada Y en píxeles
        :param u: coordenada U del sprite en Pyxel
        :param v: coordenada V del sprite en Pyxel
        :param tamano: tamaño de la casilla en píxeles (por defecto 16)
        """
        # Comprobamos los tipos de los atributos de solo lectura
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Las coordenadas x e y deben ser enteros")
        if not isinstance(u, int) or not isinstance(v, int):
            raise TypeError("Las coordenadas u y v deben ser enteros")
        if not isinstance(tamano, int):
            raise TypeError("El tamaño debe ser un entero")
        if tamano <= 0:
            raise ValueError("El tamaño debe ser mayor que 0")

        # Atributos privados (solo se leen mediante @property, sin setter)
        self.__x = x
        self.__y = y
        self.__u = u
        self.__v = v
        self.__tamano = tamano

    @property
    def x(self) -> int:
        """Devuelve la coordenada X del cubo de basura.

        :return: coordenada X en píxeles
        """
        return self.__x

    @property
    def y(self) -> int:
        """Devuelve la coordenada Y del cubo de basura.

        :return: coordenada Y en píxeles
        """
        return self.__y

    def interactuar(self, chef) -> bool:
        """Gestiona la acción de un chef frente al cubo de basura.

        Si el chef lleva un plato lleno, vacía su contenido manteniendo
        el plato en sus manos.

        :param chef: objeto de la clase Chef que realiza la acción
        :return: True si se vació el plato, False en caso contrario
        """
        # Variable local para el objeto que lleva el chef
        plato = chef.objeto_en_mano

        # Comprobamos con isinstance que sea un Plato y que no esté vacío
        if isinstance(plato, Plato) and not plato.esta_vacio():
            plato.vaciar()
            return True

        return False

    def dibujar(self):
        """Dibuja el cubo de basura en la pantalla."""
        pyxel.blt(self.__x, self.__y, 0, self.__u, self.__v, self.__tamano, self.__tamano)
