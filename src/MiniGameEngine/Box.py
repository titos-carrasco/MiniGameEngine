from MiniGameEngine.GameObject import GameObject


class Box(GameObject):
    """
    Clase que representa un Rectángulo y que se puede utilizar como un colisionador transparente.
    """

    def __init__(
        self,
        x: float,
        y: float,
        width: int,
        height: int,
        layer: int,
        tipo: str,
        line_width: int = 1,
        line_color: str = "black",
        fill_color: str = None,
    ):
        """
        Crea un objeto de la clase Rectangle.

        Args:
            x (float): Coordenada x del rectángulo.
            y (float): Coordenada y del rectángulo.
            width (int): Ancho del rectángulo.
            height (int): Alto del rectángulo.
            layer (int): Capa en que se colocará este sprite.
            tipo (str): Tipo de rectángulo.
            line_width (int, opcional): Ancho de la línea del rectángulo (por defecto 1).
            line_color (str, opcional): Color de la línea del rectángulo (por defecto "black").
            fill_color (str, opcional): Color de relleno del rectángulo (por defecto None).
        """
        width, height = int(width), int(height)
        assert width > 0, "Box(): width debe ser mayor que 0."
        assert height > 0, "Box(): height debe ser mayor que 0."

        super().__init__(x, y, width, height, layer=layer, tipo=tipo)

        self._element = self._canvas.create_rectangle(
            int(x),
            int(y),
            int(x) + width - 1,
            int(y) + height - 1,
            width=line_width,
            outline=line_color,
            fill=fill_color,
            state="disabled",
        )

        self._addToGame()

    def setDimension(self, width: int, height: int):
        """
        Modifica tamaño del rectángulo.

        Args:
            width (int): Ancho del rectángulo.
            height (int): Alto del rectángulo.
        """
        assert width > 0, "Box.setDimension(): width debe ser mayor que 0."
        assert height > 0, "Box.setDimension(): height debe ser mayor que 0."

        self._setDimension(int(width), int(height))

        x1, y1, x2, y2 = self.getCoords()
        self._canvas.coords(self._element, int(x1), int(y1), int(x2), int(y2))
