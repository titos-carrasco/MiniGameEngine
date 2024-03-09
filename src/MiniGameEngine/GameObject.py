from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.Rectangle import Rectangle


class GameObject:
    """Clase que representa un objeto dentro del juego."""

    _counter_ = 0

    def __init__(
        self, x: float, y: float, width: int, height: int, layer: int, tipo: str
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
        """
        width, height, layer = int(width), int(height), int(layer)
        assert width > 0, "GameObject(): Ancho debe ser mayor que 0."
        assert height > 0, "GameObject(): Alto debe ser mayor que 0."
        assert 1 <= layer <= 9999, "GameObject(): Layer debe estar entre 1 y 9999."

        self.gw = GameWorld._getInstance()
        self._canvas = self.gw._getCanvas()
        self._add_gobject = self.gw._addGObject
        self._del_gobject = self.gw._delGObject

        self._element = 0

        self._rect = Rectangle(x, y, width, height)
        self._layer = layer
        self._tipo = tipo
        self._can_collide = False

    # ---

    def getX(self) -> float:
        """
        Obtiene la coordenada x actual del objeto.

        Returns:
            float: Coordenada x del objeto.
        """
        return self._rect.getX()

    def getY(self) -> float:
        """
        Obtiene la coordenada y actual del objeto.

        Returns:
            float: Coordenada y del objeto.
        """
        return self._rect.getY()

    def getPosition(self) -> (float, float):
        """Obtiene las coordenadas x e y del objeto.

        Returns:
            (float, float): Las coordenadas x e y del objeto.
        """
        return self._rect.getPosition()

    def getCoords(self) -> (float, float, float, float):
        """
        Retorna las coordenadas del rectángulo que rodea al objeto.

        Returns:
            float, float, float, float: El rectángulo que rodea al objeto.
        """
        return self._rect.getCoords()

    def getWidth(self) -> int:
        """
        Obtiene el ancho del objeto.

        Returns:
            int: Ancho del objeto.
        """
        return self._rect.getWidth()

    def getHeight(self) -> int:
        """
        Obtiene la altura del objeto.

        Returns:
            int: Altura del objeto.
        """
        return self._rect.getHeight()

    def getDimension(self) -> (int, int):
        """
        Retorna la dimensión del objeto.

        Returns:
            (int, int): El ancho y alto del objeto.
        """
        return self._rect.getDimension()

    def getElement(self) -> int:
        """
        Retorna el identificador del elemento visual de este objeto dentro del canvas.

        Returns:
            int: El identificador del elemento
        """
        return self._element

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

    def setX(self, x: float):
        """
        Establece la cooordenada x del objeto.

        Args:
            x (float): La coordenada x del objeto.
        """
        self._rect.setX(x)
        self._canvas.moveto(
            self._element, int(self._rect.getX()), int(self._rect.getY())
        )

    def setY(self, y: float):
        """
        Establece la cooordenada y del objeto.

        Args:
            y (float): La coordenada y del objeto.
        """
        self._rect.setY(y)
        self._canvas.moveto(
            self._element, int(self._rect.getX()), int(self._rect.getY())
        )

    def setPosition(self, x: float, y: float):
        """
        Establece la posición del sprite en el mundo de juego.

        Args:
            x (float): Nueva coordenada x del sprite.
            y (float): Nueva coordenada y del sprite.
        """
        self._rect.setPosition(x, y)
        self._canvas.moveto(
            self._element, int(self._rect.getX()), int(self._rect.getY())
        )

    def setVisibility(self, visible: bool):
        """
        Cambia visibilidad del objeto

        Args:
            visible (bool): True lo muestra. False lo oculta
        """
        state = "disabled" if visible else "hidden"
        self._canvas.itemconfig(self._element, state=state)

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

    def collides(self, gobj) -> bool:
        """
        Determina si este GameObject colisiona con otro.

        Args:
            gobj (GameObject): GameObject a detectar si colisiona con este GameObject.

        Returns:
            bool: True si colisiona. False en caso contrario.
        """
        return self._rect.intersects(gobj._rect)

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
        self._del_gobject(self)

    # --

    def _addToGame(self):
        """
        Agrega este GameObject a la lista de objetos del juego
        """
        GameObject._counter_ = GameObject._counter_ + 1
        tag = f"{self._layer:04d}-{GameObject._counter_:06d}"
        self._canvas.itemconfig(self._element, tags=(tag,))

        self._add_gobject(self)

    def _setDimension(self, width: int, height: int):
        width, height = int(width), int(height)
        assert width > 0, "GameObject.setDimension(): Ancho debe ser mayor que 0."
        assert height > 0, "GameObject.setDimension(): Alto debe ser mayor que 0."

        self._rect.setDimension(width, height)

    def _kill(self):
        self._canvas.delete(self._element)
        del self._rect
