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
        super().__init__(x, y, width=1, height=1, layer=layer, tipo=tipo)

        img = self.gw.loadImage(image_path)
        width, height = img.width(), img.height()

        self._element = self._canvas.create_image(
            int(x),
            int(y),
            image=img,
            anchor="nw",
            state="disabled",
        )

        self._setDimension(width, height)
        self._addToGame()

        self._border = None
        if debug:
            self._border = Box(
                x, y, width, height, layer, tipo="Borde", line_width=1, line_color="red"
            )

    def setShape(self, image_path: str):
        """
        Cambia la imagen del sprite.

        Args:
            imagePath (str): Archivo con la nueva imagen para el sprite.
        """
        img = self.gw.loadImage(image_path)
        width, height = img.width(), img.height()

        self._canvas.itemconfig(self._element, image=img)
        self._setDimension(width, height)

    def setX(self, x: float):
        """
        Establece la cooordenada x del objeto.

        Args:
            x (float): La coordenada x del objeto.
        """
        if self._border:
            self._border.setX(x)
        super().setX(x)

    def setY(self, y: float):
        """
        Establece la cooordenada y del objeto.

        Args:
            y (float): La coordenada y del objeto.
        """
        if self._border:
            self._border.setY(y)
        super().setY(y)

    def setPosition(self, x: float, y: float):
        """
        Establece la posición del sprite en el mundo de juego.

        Args:
            x (float): Nueva coordenada x del sprite.
            y (float): Nueva coordenada y del sprite.
        """
        if self._border:
            self._border.setPosition(x, y)
        super().setPosition(x, y)

    # ---

    def _kill(self):
        if self._border:
            self._border.delete()
            del self._border

        super()._kill()
