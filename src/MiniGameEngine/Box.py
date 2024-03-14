from MiniGameEngine.GameObject import GameObject


class Box(GameObject):
    """
    Clase que representa una caja y que se puede utilizar como un colisionador transparente.
    """

    def __init__(
        self,
        x: float,
        y: float,
        width: int,
        height: int,
        layer: int,
        tipo: str,
        border: int = 1,
        border_color: str = "black",
        fill_color: str = None,
        debug: bool = False,
    ):
        """
        Crea un objeto de la clase Box.

        Args:
            x (float): Coordenada x de la caja.
            y (float): Coordenada y de la caja.
            width (int): Ancho de la caja.
            height (int): Alto de la caja.
            layer (int): Capa en que se colocará este objeto.
            tipo (str): Tipo de caja.
            border (int, opcional): Ancho de la línea de la caja (por defecto 1).
            border_color (str, opcional): Color de la línea de la caja (por defecto "black").
            fill_color (str, opcional): Color de relleno de la caja (por defecto None).
            debug (bool, opcional): True para mostrar información del objeto.
        """
        super().__init__(x, y, width, height, layer=layer, tipo=tipo, debug=debug)
        width, height = self.getDimension()

        # ajustamos el ancho del borde
        border = int(border)
        if border == 0:
            line_color = None

        # necesario por la forma en que tk maneja el rectángulo
        fix = int((border + 1) / 2)

        # creamos la caja
        self._item = self._canvas.create_rectangle(
            int(x + border - fix),
            int(y + border - fix),
            int(x + width - fix),
            int(y + height - fix),
            width=border,
            outline=border_color,
            fill=fill_color,
            state="disabled",
        )

        # la agregamos al juego
        self._addToGame()

    def setX(self, x: float):
        """
        Establece la cooordenada x de la caja.

        Args:
            x (float): La coordenada x de la caja.
        """
        self._setX(x)
        x1, y1, x2, y2 = self.getCoords()
        self._canvas.coords(self._item, int(x1), int(y1), int(x2), int(y2))

    def setY(self, y: float):
        """
        Establece la cooordenada y de la caja.

        Args:
            y (float): La coordenada y de la caja.
        """
        self._setY(y)
        x1, y1, x2, y2 = self.getCoords()
        self._canvas.coords(self._item, int(x1), int(y1), int(x2), int(y2))

    def setPosition(self, x: float, y: float):
        """
        Establece la posición de la caja en el mundo de juego.

        Args:
            x (float): Nueva coordenada x de la caja.
            y (float): Nueva coordenada y de la caja.
        """
        self._setPosition(x, y)
        x1, y1, x2, y2 = self.getCoords()
        self._canvas.coords(self._item, int(x1), int(y1), int(x2), int(y2))

    def setDimension(self, width: int, height: int):
        """
        Modifica tamaño de la caja.

        Args:
            width (int): Ancho de la caja.
            height (int): Alto de la caja.
        """
        self._setDimension(width, height)

        x1, y1, x2, y2 = self.getCoords()
        self._canvas.coords(self._item, int(x1), int(y1), int(x2), int(y2))
