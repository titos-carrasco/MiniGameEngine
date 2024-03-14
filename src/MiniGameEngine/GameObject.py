from MiniGameEngine.GameWorld import GameWorld


class GameObject:
    """Clase que representa un objeto dentro del juego."""

    _counter_ = 0

    def __init__(
        self,
        x: float,
        y: float,
        width: int,
        height: int,
        layer: int,
        tipo: str,
        debug: bool = False,
    ):
        """
        Crea un objeto de la clase GameObject.

        Args:
            x (float): Coordenada x del objeto.
            y (float): Coordenada y del objeto.
            width (int): Ancho del objeto.
            height (int): Alto del objeto.
            layer (int): Capa en que se colocará este objeto (1-9999).
            tipo (str): Tipo del objeto.
            debug (bool, opcional): True para mostrar información del objeto.
        """
        assert width >= 1, "GameObject.init(): Ancho debe ser mayor o igual a 1."
        assert height >= 1, "GameObject.init(): Alto debe ser mayor o igual a 1."

        self._width = int(width)
        self._height = int(height)
        self._x1 = x
        self._y1 = y
        self._x2 = self._x1 + self._width - 1
        self._y2 = self._y1 + self._height - 1

        assert 1 <= layer <= 9999, "GameObject(): Layer debe estar entre 1 y 9999."
        self._layer = int(layer)

        self._tipo = tipo
        self._debug = debug
        self._border = None

        self._item = 0
        self._can_collide = False

        self.gw = GameWorld._getInstance()
        self._canvas = self.gw._getCanvas()

    # ---

    def getX(self) -> float:
        """
        Obtiene la coordenada x actual del objeto.

        Returns:
            float: Coordenada x del objeto.
        """
        return self._x1

    def getY(self) -> float:
        """
        Obtiene la coordenada y actual del objeto.

        Returns:
            float: Coordenada y del objeto.
        """
        return self._y1

    def getPosition(self) -> (float, float):
        """Obtiene las coordenadas x e y del objeto.

        Returns:
            (float, float): Las coordenadas x e y del objeto.
        """
        return self._x1, self._y1

    def getCoords(self) -> (float, float, float, float):
        """
        Retorna las coordenadas del rectángulo que rodea al objeto.

        Returns:
            float, float, float, float: El rectángulo que rodea al objeto.
        """
        return self._x1, self._y1, self._x2, self._y2

    def getWidth(self) -> int:
        """
        Obtiene el ancho del objeto.

        Returns:
            int: Ancho del objeto.
        """
        return self._width

    def getHeight(self) -> int:
        """
        Obtiene la altura del objeto.

        Returns:
            int: Altura del objeto.
        """
        return self._height

    def getDimension(self) -> (int, int):
        """
        Retorna la dimensión del objeto.

        Returns:
            (int, int): El ancho y alto del objeto.
        """
        return self._width, self._height

    def getItem(self) -> int:
        """
        Retorna el identificador del componente visual de este objeto dentro del canvas.

        Returns:
            int: El identificador del item
        """
        return self._item

    def getLayer(self) -> int:
        """
        Retorna el número de la capa de este objeto

        Returns:
            int: La capa en donde se ubica este objeto.
        """
        return self._layer

    def getTipo(self) -> str:
        """
        Obtiene el tipo del objeto.

        Returns:
            str: Tipo del objeto.
        """
        return self._tipo

    def setVisibility(self, visible: bool):
        """
        Cambia visibilidad del objeto

        Args:
            visible (bool): True lo muestra. False lo oculta
        """
        state = "disabled" if visible else "hidden"
        self._canvas.itemconfig(self._item, state=state)

    def setCollisions(self, enable: bool):
        """
        Habilita o deshabilita participar del procesamiento de colisiones.

        Args:
            enable (bool): True para habilitar, False para deshabilitar.
        """
        self._can_collide = enable

    def canCollide(self) -> bool:
        """
        Determina si tiene habilitadas las colisiones

        Returns:
            bool: True si las colisiones están habilitadas. False en caso contrario
        """
        return self._can_collide

    def intersects(self, gobj) -> bool:
        """
        Determina si este objeto intersecta con otro.

        Args:
            gobj (GameObject): El objeto contra el que se verificará la intersección.

        Returns:
            bool: True si este objeto intersecta al otro. False en caso contrario
        """
        rx1, ry1, rx2, ry2 = gobj.getCoords()
        return (
            self._x1 <= rx2 and rx1 <= self._x2 and self._y1 <= ry2 and ry1 <= self._y2
        )

    def intersection(self, gobj) -> (int, int, int, int):
        """
        Determina las coordenadas de intersección de este objeto con otro.

        Args:
            gobj (GameObject): El objeto contra el que se determinará la intersección.

        Returns:
            (int, int, int, int): Las coordenadas de intersección. None si no existe intersección
        """
        x1, y1, x2, y2 = gobj.getCoords()

        x1 = max(self._x1, x1)
        y1 = max(self._y1, y1)
        x2 = min(self._x2, x2)
        y2 = min(self._y2, y2)
        if y1 <= y2 and x1 <= x2:
            return (x1, y1, x2 - x1 + 1, y2 - y1 + 1)
        return None

    def onUpdate(self, dt: float):
        """
        Llamado en cada actualización del juego para el objeto.

        Args:
            dt (float): Tiempo en segundos desde la ultima llamada.
        """

    def onCollision(self, dt: float, gobj):
        """
        Llamado cuando el objeto colisiona con otro objeto.

        Args:
            dt (float): Tiempo en segundos desde la ultima llamada.
            gobj (GameObject): Objeto con el que colisiona.
        """

    def delete(self):
        """Elimina el objeto del mundo de juego."""
        self.gw._delGObject(self)

    # --

    def _kill(self):
        if self._border:
            self._border.delete()
            del self._border
            del self._debug

        self._canvas.delete(self._item)
        del self._canvas
        del self.gw

    def _addToGame(self):
        GameObject._counter_ = GameObject._counter_ + 1

        tag = f"{self._layer:04d}-{GameObject._counter_:06d}"
        self._canvas.itemconfig(self._item, tags=(tag,))

        self.gw._addGObject(self)

        if self._debug:
            from MiniGameEngine.Box import Box

            self._border = Box(
                self._x1,
                self._y1,
                self._width,
                self._height,
                self._layer,
                tipo="",
                border=1,
                border_color="red",
            )

    def _setX(self, x):
        self._x1 = x
        self._x2 = self._x1 + self._width - 1

        if self._border:
            self._border.setX(x)

    def _setY(self, y):
        self._y1 = y
        self._y2 = self._y1 + self._height - 1

        if self._border:
            self._border.setY(y)

    def _setPosition(self, x, y):
        self._x1 = x
        self._y1 = y
        self._x2 = self._x1 + self._width - 1
        self._y2 = self._y1 + self._height - 1

        if self._border:
            self._border.setPosition(x, y)

    def _setDimension(self, width, height):
        assert (
            width >= 1
        ), "GameObject._setDimension(): Ancho debe ser mayor o igual a 1."
        assert (
            height >= 1
        ), "GameObject._setDimension(): Alto debe ser mayor o igual a 1."

        self._width = int(width)
        self._x2 = self._x1 + self._width - 1

        self._height = int(height)
        self._y2 = self._y1 + self._height - 1

        if self._border:
            self._border.setDimension(self._width, self._height)
