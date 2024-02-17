from MiniGameEngine.GameWorld import GameWorld


class GameObject:
    """Clase que representa un objeto dentro del juego."""

    def __init__(self, x: int, y: int, layer: int, tipo: str):
        """
        Crea un objeto de la clase GameObject.

        Args:
            x (int): Coordenada x del objeto.
            y (int): Coordenada y del objeto.
            layer (int): Capa en que se colocará este objeto.
            tipo (str): Tipo del objeto.
        """
        self._gw = GameWorld._getInstance()
        self._canvas = self._gw._getCanvas()

        self._element = None

        self._x = int(x)
        self._y = int(y)
        self._width = 0
        self._height = 0
        self._layer = layer
        self._tipo = tipo
        self._can_collide = False

        self._gw._addGObject(self)

    def _getGameWorld(self):
        return self._gw

    def _getCanvas(self):
        return self._canvas

    def _getElement(self):
        return self._element

    def _setElement(self, element):
        self._element = element

    def _setDimension(self, width: int, height: int):
        self._width = int(width) if width >= 0 else 0
        self._height = int(height) if height >= 0 else 0

    # ---

    def getX(self) -> int:
        """
        Obtiene la coordenada x actual del objeto.

        Returns:
            int: Coordenada x del objeto.
        """
        return self._x

    def getY(self) -> int:
        """
        Obtiene la coordenada y actual del objeto.

        Returns:
            int: Coordenada y del objeto.
        """
        return self._y

    def getPosition(self) -> (int, int):
        """Obtiene las coordenadas x e y del objeto.

        Returns:
            (int, int): Las coordenadas x e y del objeto.
        """
        return self._x, self._y

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
        Retorna las dimensiones del objeto.

        Returns:
            (int, int): El ancho y alto del objeto.
        """
        return self._width, self._height

    def getLayer(self) -> int:
        """
        Obtiene la capa en la que se encuentra este objeto.

        Returns:
            int: La capa en que se encuentra este objeto.
        """
        return self._layer

    def getTipo(self) -> str:
        """
        Obtiene el tipo del objeto.

        Returns:
            str: Tipo del objeto.
        """
        return self._tipo

    def setX(self, x: int):
        """
        Establece la cooordenada x del objeto.

        Args:
            x (int): La coordenada x del objeto.
        """
        x = int(x)
        dx = x - self._x
        dy = 0
        self._canvas.move(self._element, dx, dy)
        self._x = x

    def setY(self, y: int):
        """
        Establece la cooordenada y del objeto.

        Args:
            y (int): La coordenada y del objeto.
        """
        y = int(y)
        dx = 0
        dy = y - self._y
        self._canvas.move(self._element, dx, dy)
        self._y = y

    def setPosition(self, x: int, y: int):
        """
        Establece la posición del sprite en el mundo de juego.

        Args:
            x (int): Nueva coordenada x del sprite.
            y (int): Nueva coordenada y del sprite.
        """
        x, y = int(x), int(y)
        dx = x - self._x
        dy = y - self._y
        self._canvas.move(self._element, dx, dy)
        self._x, self._y = x, y

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

    def collides(self, obj) -> bool:
        """
        Determina si este GameObject colisiona con otro.

        Args:
            obj (GameObject): GameObject a detectar si colisiona con este GameObject.

        Returns:
            bool: True si colisiona. False en caso contrario.
        """
        o1, o2 = self, obj

        o1x1 = o1._x
        o1y1 = o1._y
        o1x2 = o1x1 + o1._width - 1
        o1y2 = o1y1 + o1._height - 1

        o2x1 = o2._x
        o2y1 = o2._y
        o2x2 = o2x1 + o2._width - 1
        o2y2 = o2y1 + o2._height - 1

        return o1x1 <= o2x2 and o2x1 <= o1x2 and o1y1 <= o2y2 and o2y1 <= o1y2

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

    def destroy(self):
        """Elimina el objeto del mundo de juego."""
        self._canvas.delete(self._element)
        del self._element

        self._gw._delGObject(self)
        del self._canvas
        del self._gw

    # ---

    def getWorldWidth(self) -> int:
        """
        Obtiene el ancho del mundo de juego.

        Returns:
            int: Ancho del mundo de juego.
        """
        return self._gw.getWidth()

    def getWorldHeight(self) -> int:
        """
        Obtiene la altura del mundo de juego.

        Returns:
            int: Altura del mundo de juego.
        """
        return self._gw.getHeight()

    def isPressed(self, key_name: str) -> bool:
        """
        Verifica si una tecla específica está siendo presionada.

        Args:
            key_name (str): Nombre de la tecla a verificar.

        Returns:
            bool: True si la tecla está presionada, False en caso contrario.
        """
        return self._gw.isPressed(key_name)
