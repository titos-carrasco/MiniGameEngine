class Rectangle:
    """
    Clase para manejar rectángulos
    """

    def __init__(self, x: float, y: float, width: int, height: int):
        """
        Crea un objeto del tipo Rectángulo con centro en su esquina superior izquierda.

        Args:
            x (float): Coordenada x del rectángulo.
            y (float): Coordenada y del rectángulo.
            width (int): Ancho del rectángulo.
            height (int): Alto del rectángulo.
        """
        width, height = int(width), int(height)
        assert width > 0, "Rectangle(): Ancho debe ser mayor que 0."
        assert height > 0, "Rectangle(): Alto debe ser mayor que 0."

        self._width = width
        self._height = height
        self._x1 = x
        self._y1 = y
        self._x2 = self._x1 + self._width - 1
        self._y2 = self._y1 + self._height - 1

    def getX(self) -> float:
        """
        Retorna la coordenada x de la esquina superior izquierda del rectángulo.

        Returns:
            float: La coordenada x.
        """
        return self._x1

    def getY(self) -> float:
        """
        Retorna la coordenada y de la esquina superior izquierda del rectángulo.

        Returns:
            float: La coordenada y.
        """
        return self._y1

    def getPosition(self) -> (float, float):
        """
        Retorna la coordenada x, y de la esquina superior izquierda del rectángulo

        Returns:
            float, float: La coordenada x, y.
        """
        return self._x1, self._y1

    def getCoords(self) -> (float, float, float, float):
        """
        Retorna las coordenadas superior izquierda (x1, y1) e inferior derecha (x2, y2) del rectángulo.

        Returns:
            x1 (float): Coordena x1 del objeto.
            y1 (float): Coordena y1 del objeto.
            x2 (float): Coordena x2 del objeto.
            y2 (float): Coordena y2 del objeto.
        """
        return self._x1, self._y1, self._x2, self._y2

    def getWidth(self) -> int:
        """
        Retorna el ancho del rectángulo.

        Returns:
            int: El ancho del rectángulo.
        """
        return self._width

    def getHeight(self) -> int:
        """
        Retorna el alto del rectángulo.

        Returns:
            int: El alto del rectángulo.
        """
        return self._height

    def getDimension(self) -> (int, int):
        """
        Retorna el ancho y alto del rectángulo.

        Returns:
            int: El ancho del rectángulo.
            int: El alto del rectángulo.
        """
        return self._width, self._height

    # ---

    def setX(self, x: float):
        """
        Establece la cooordenada x del objeto.

        Args:
            x (float): La coordenada x del objeto.
        """
        self._x1 = x
        self._x2 = self._x1 + self._width - 1

    def setY(self, y: float):
        """
        Establece la cooordenada y del objeto.

        Args:
            y (float): La coordenada y del objeto.
        """
        self._y1 = y
        self._y2 = self._y1 + self._height - 1

    def setPosition(self, x: float, y: float):
        """
        Establece la posición del sprite en el mundo de juego.

        Args:
            x (int): Nueva coordenada x del sprite.
            y (int): Nueva coordenada y del sprite.
        """
        self._x1 = x
        self._y1 = y
        self._x2 = self._x1 + self._width - 1
        self._y2 = self._y1 + self._height - 1

    def setWidth(self, width: int):
        """
        Establece el ancho del rectángulo.

        Args:
            width (int): El ancho del rectángulo
        """
        width = int(width)
        assert width > 0, "Rectangle.setWidth(): Ancho debe ser mayor que 0."

        self._width = width
        self._x2 = self._x1 + self._width - 1

    def setHeight(self, height: int):
        """
        Establece el alto del rectángulo.

        Args:
            height (int): El alto del rectángulo
        """
        height = int(height)
        assert height > 0, "Rectangle.setHeight(): Alto debe ser mayor que 0."

        self._height = height
        self._y2 = self._y1 + self._height - 1

    def setDimension(self, width: int, height: int):
        """
        Establece el acho y alto del rectángulo.

        Args:
            width (int): El ancho del rectángulo
            height (int): El alto del rectángulo.
        """
        width, height = int(width), int(height)
        assert width > 0, "Rectangle.setDimension(): Ancho debe ser mayor que 0."
        assert height > 0, "Rectangle.setDimension(): Alto debe ser mayor que 0."

        self.setWidth(width)
        self.setHeight(height)

    # ---
    def intersects(self, rect) -> bool:
        """
        Determina si este rectángulo intersecta con otro.

        Args:
            rect (Rectangle): El rectángulo contra el que se verificará la intersección.

        Returns:
            bool: True si este rectángulo intersecta al otro. False en caso contrario
        """
        rx1, ry1, rx2, ry2 = rect.getCoords()
        return (
            self._x1 <= rx2 and rx1 <= self._x2 and self._y1 <= ry2 and ry1 <= self._y2
        )

    def intersection(self, rect):
        """
        Determina el rectángulo de intersección de este rectángulo con otro.

        Args:
            rect (Rectangle): El rectángulo contra el que se determinará la intersección.

        Returns:
            Rectangle: El rectángulo de intersección.
        """
        rx1, ry1, rx2, ry2 = rect.getCoords()

        x1 = max(self._x1, rx1)
        y1 = max(self._y1, ry1)
        x2 = min(self._x2, rx2)
        y2 = min(self._y2, ry2)
        return Rectangle(x1, y1, round(x2 - x1), round(y2 - y1))
