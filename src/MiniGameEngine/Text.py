from MiniGameEngine.GameObject import GameObject


class Text(GameObject):
    """Clase que representa un GameObject definido por un texto."""

    def __init__(
        self,
        x: float,
        y: float,
        layer: int,
        tipo: str = None,
        text: str = None,
        font: str = "Arial 12",
        color: str = "black",
        debug: bool = False,
    ):
        """
        Crea una un objeto de la clase Text.

        Args:
            x (float): Coordenada x del texto.
            y (float): Coordenada y del texto.
            layer (int): Capa en que se colocará este texto.
            tipo (str, opcional): Tipo del objeto.
            text (str, opcional): Texto para este objeto
            font (str, opcional): Font a utilizar para el texto (por defecto es "Arial 12").
            color (str, opcional): Color a utilizar para el texto (por defecto es "black").
            debug (bool, opcional): True para mostrar información del objeto.
        """
        super().__init__(x, y, width=1, height=1, layer=layer, tipo=tipo, debug=debug)

        # creamos el texto
        self._item = self._canvas.create_text(
            int(x),
            int(y),
            text=text,
            font=font,
            fill=color,
            anchor="nw",
            state="disabled",
        )

        # registramos su tamaño
        self._updateDimension()

        # lo agregamos al juego
        self._addToGame()

    def setX(self, x: float):
        """
        Establece la cooordenada x del objeto.

        Args:
            x (float): La coordenada x del objeto.
        """
        self._setX(x)
        x, y = self.getPosition()
        self._canvas.moveto(self._item, int(x), int(y))

    def setY(self, y: float):
        """
        Establece la cooordenada y del objeto.

        Args:
            y (float): La coordenada y del objeto.
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

    def setText(self, text: str):
        """
        Cambia el texto del objeto.

        Args:
            text (str): El nuevo texto del objeto.
        """
        self._canvas.itemconfig(self._item, text=text)
        self._updateDimension()

    def setFont(self, font: str):
        """
        Cambia el Tipo de letra, tamaño y atributo del texto del objeto.
        El nuevo font se puede especificar como "Arial 10 italica bold"

        Args:
            font (str): El nuevo tipo de letra, tamaño y atributo del texto del objeto.
        """
        self._canvas.itemconfig(self._element, font=font)
        self._updateDimension()

    def setColor(self, color: str):
        """
        Cambia el color del texto del objeto.

        Args:
            color (str): El nuevo color para el texto del objeto.
        """
        self._canvas.itemconfig(self._element, fill=color)

    # ---

    def _updateDimension(self):
        bbox = self._canvas.bbox(self._item)
        width = bbox[2] - bbox[0] + 1
        height = bbox[3] - bbox[1] + 1

        self._setDimension(width, height)
