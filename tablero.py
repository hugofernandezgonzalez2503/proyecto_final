# Importamos la biblioteca pyxel
import pyxel
# Importamos la clase Chef para poder utilizarla en la clase Tablero
from chef import Chef


class Tablero:
    """Esta clase contiene un tablero sencillo"""
    def __init__(self, ancho: int, alto: int):
        """Método que crea el tablero.
        :param ancho: El ancho del tablero
        :param alto: La altura del tablero
        """
        # Establecimiento de los atributos
        self.ancho = ancho
        self.alto = alto
        # El tablero contendrá un Chef en el centro, por lo que uno de
        # los atributos del tablero será un objeto Chef. Ten en cuenta que lo que se encuentra
        # en el centro del tablero es la esquina superior izquierda del Chef.
        self.chef = Chef(self.ancho // 2, self.alto // 2)
        # En el init también inicializamos Pyxel
        # Esta instrucción se utiliza para inicializar Pyxel; consulta la API para obtener más
        # parámetros
        pyxel.init(self.ancho, self.alto, title="Demostración del juego Pyxel",
                   display_scale=4)
        # Carga del archivo pyxres con las imágenes
        pyxel.load("assets/example.pyxres")
        # Ejecución del juego; esto llamará a los métodos update y draw en cada
        # fotograma; consulta la API para obtener más información
        pyxel.run(self.update, self.draw)

    # Propiedades y setters
    @property
    def ancho(self) -> int:
        return self.__ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @ancho.setter
    def ancho(self, ancho: int):
        if not isinstance(ancho, int):
            raise TypeError("El ancho tiene que ser un entero")
        elif ancho < 1:
            raise ValueError("El ancho tiene que ser un entero positivo")
        else:
            self.__ancho = ancho

    @alto.setter
    def alto(self, alto: int):
        if not isinstance(alto, int):
            raise TypeError("El alto tiene que ser un entero")
        elif alto < 1:
            raise ValueError("El alto tiene que ser un entero positivo")
        else:
            self.__alto = alto

    def update(self):
        """Este es el método de Pyxel que se ejecuta en cada iteración del
        juego (cada fotograma). Aquí debes incluir todo el código que deba
        ejecutarse en cada fotograma. Por ahora, solo contiene la lógica para salir del
        programa si se pulsa una tecla y para mover el chef si pulsamos una flecha"""
        # Para salir del juego
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        # Para mover el chef
        if pyxel.btn(pyxel.KEY_LEFT):
            self.chef.mover("izquierda", self.ancho)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.chef.mover("derecha", self.ancho)
        if pyxel.btn(pyxel.KEY_UP):
            self.chef.mover("arriba", self.alto)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.chef.mover("abajo", self.alto)

    def draw(self):
        """Este es el método de Pyxel que se ejecuta en cada iteración del
        juego (cada fotograma). Aquí debes colocar todo el código para dibujar los
        sprites del juego.
        """
        # Borrar la pantalla anterior
        pyxel.cls(0)
        # Dibujar al chef. Los parámetros de pyxel.blt son (x, y, tuple_de_sprite)
        # El asterisco (*) se utiliza para desempaquetar la tupla del sprite
        pyxel.blt(self.chef.x, self.chef.y, *self.chef.imagen)
        # Un texto para mostrar la posición del chef; los parámetros de
        # pyxel.text son (x, y, texto, color)
        pyxel.text(10, 10, f"({self.chef.x}, {self.chef.y})", 7)
