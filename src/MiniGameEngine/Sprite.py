from MiniGameEngine.GameObject import GameObject
from MiniGameEngine.Box import Box


class Sprite(GameObject):
    """Clase que representa un GameObject definido por una imagen."""

    def __init__(
        self,
        x: float,
        y: float,
        layer: int,
        tipo: str,
        image_path: str,
        debug: bool = False,
    ):
        """
        Crea un objeto de la clase Sprite.

        Args:
            x (float): Coordenada x del sprite.
            y (float): Coordenada y del sprite.
            layer (int): Capa en que se colocará este sprite.
            tipo (str): Tipo de sprite.
            imagePath (str): Archivo con la imagen del sprite.
            debug (bool, opcional): True para mostrar información del objeto.
        """
        super().__init__(x, y, width=1, height=1, layer=layer, tipo=tipo, debug=debug)

        # creamos la imagen
        img = self.gw.loadImage(image_path)
        width, height = img.width(), img.height()
        self._item = self._canvas.create_image(
            int(x),
            int(y),
            image=img,
            anchor="nw",
            state="disabled",
        )

        # registramos su tamaño
        self._setDimension(width, height)

        # lo agregaos al juego
        self._addToGame()

    def setX(self, x: float):
        """
        Establece la cooordenada x del sprite.

        Args:
            x (float): La coordenada x del sprite.
        """
        self._setX(x)
        x, y = self.getPosition()
        self._canvas.moveto(self._item, int(x), int(y))

    def setY(self, y: float):
        """
        Establece la cooordenada y del sprite.

        Args:
            y (float): La coordenada y del sprite.
        """
        self._setY(y)
        x, y = self.getPosition()
        self._canvas.moveto(self._item, int(x), int(y))

    def setPosition(self, x: float, y: float):
        """
        Establece la posición del sprite en el mundo de juego.

        Args:
            x (float): Nueva coordenada x del sprite.
            y (float): Nueva coordenada y del sprite.
        """
        self._setPosition(x, y)
        x, y = self.getPosition()
        self._canvas.moveto(self._item, int(x), int(y))

    def setShape(self, image_path: str):
        """
        Cambia la imagen del sprite.

        Args:
            imagePath (str): Archivo con la nueva imagen para el sprite.
        """
        img = self.gw.loadImage(image_path)
        width, height = img.width(), img.height()

        self._canvas.itemconfig(self._item, image=img)
        self._setDimension(width, height)
