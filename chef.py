import random


class Chef:
    """ Una primera versión de la clase «Chef» para el proyecto final. Solo
    contiene propiedades y métodos de asignación. Puede que tenga un plato o puede que no """
    def __init__(self, x:int, y:int, imagen_x:int, imagen_y:int, plato:bool):
        """self.x indica la posicion x del chef en el tablero
        self.y indica la posicion y del chef en el tablero
        imagen_x e imagen_y son las coordenadas para elegir la imagen que queremos usar de resources"""
        self.x=x
        self.y=y
        self.imagen_x=imagen_x
        self.imagen_y=imagen_y
        self.plato=plato
        self.imagen = (0, imagen_x, imagen_y, 16, 16)
        valor = random.randint(0, 1)
        if valor == 1:
            self.tiene_plato = True
        else:
            self.tiene_plato = False

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def imagen(self) -> tuple:
        return self.__imagen

    @property
    def tiene_plato(self) -> bool:
        return self.__tiene_plato

    @x.setter
    def x(self, x: int):
        if not isinstance(x, int):
            raise TypeError("La posición x tiene que ser int")
        elif x < 0:
            raise ValueError("La x no puede ser negativa")
        else:
            self.__x = x

    @y.setter
    def y(self, y: int):
        if not isinstance(y, int):
            raise TypeError("La posición y tiene que ser int")
        elif y < 0:
            raise ValueError("La y no puede ser negativa")
        else:
            self.__y = y

    @imagen.setter
    def imagen(self, imagen: tuple):
        if not isinstance(imagen, tuple):
            raise TypeError("La imagen tiene que ser una tupla")
        elif len(imagen) != 5:
            raise ValueError("La imagen tiene que ser una tupla con 5 elementos")
        else:
            self.__imagen = imagen

    @tiene_plato.setter
    def tiene_plato(self, plato: bool):
        if not isinstance(plato, bool):
            raise TypeError("El atributo plato tiene que ser bool")
        else:
            self.__tiene_plato = plato


    def mover(self, direccion: str, tamaño_x_tablero: int, tamaño_y_tablero: int):
        """
        Este es un ejemplo de cómo mover al chef horizontalmente. No se tienen en cuenta
        los obstáculos del tablero.
        :param direction: una cadena que puede ser «left» o «right»
        :param board_x_size: el tamaño horizontal del tablero, para comprobar los
         límites
        """
        DIRECTIONS = ("izquierda", "derecha", "arriba", "abajo")
        # Comprobación del tipo y el valor de los parámetros
        if not isinstance(direccion, str):
            raise TypeError("La dirección debe ser una cadena de caracteres")
        elif not isinstance(tamaño_x_tablero, int):
            raise TypeError("tamaño_x_tablero debe ser un número entero")
        elif tamaño_x_tablero < 1:
            raise ValueError("El tamaño_x_tablero debe ser un entero positivo")
        elif not isinstance(tamaño_y_tablero, int):
            raise TypeError("tamaño_y_tablero debe ser un número entero")
        elif tamaño_y_tablero < 1:
            raise ValueError("El tamaño_y_tablero debe ser un entero positivo")
        elif direccion.lower() not in DIRECTIONS:
            raise ValueError("La dirección debe ser 'izquierda', 'derecha', 'arriba', 'abajo'")
        # Convertimos la dirección a minúsculas para evitar problemas con las
        # mayúsculas
        direccion = direccion.lower()
        # La posición (0, 0) del chef es la esquina superior izquierda del
        # sprite. Podemos mover al chef hacia la derecha si la coordenada x más a la derecha
        # del chef es menor que el tamaño del tablero. Será
        # la coordenada x del chef más el ancho del sprite. El
        # ancho del sprite es el cuarto elemento de la tupla de la imagen.
        if direccion == "derecha" and self.x + self.imagen[3] < tamaño_x_tablero:
           self.x += 1
    
        elif direccion == "izquierda" and self.x > 0:
          self.x -= 1

        elif direccion == "arriba" and self.y > 0:
          self.y -= 1

        elif direccion == "abajo" and self.y + self.imagen[4] < tamaño_y_tablero:
          self.y += 1
