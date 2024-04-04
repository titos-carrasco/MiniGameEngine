import tkinter as tk

from MiniGameEngine.GameWorld import GameWorld


class GameObject:
    """Clase (abstracta) que representa un objeto dentro del juego."""

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
        self._collider = [self._x1, self._y1, self._x2, self._y2]
        self._dcollider = [0, 0, 0, 0]

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

    def getCollider(self) -> (float, float, float, float):
        """_summary_

        returns:
            (float, float, float, float): Las coordenas del colisionador
        """
        return (
            self._collider[0],
            self._collider[1],
            self._collider[2],
            self._collider[3],
        )

    def setX(self, x: float):
        """
        Establece la cooordenada x del objeto.

        Args:
            x (float): La coordenada x del objeto.
        """
        if self._x1 == x:
            return

        self._x1 = x
        self._x2 = self._x1 + self._width - 1

        if self._item:
            try:
                self._canvas.coords(self._item, int(self._x1), int(self._y1))
            except tk.TclError:
                self._canvas.coords(
                    self._item,
                    int(self._x1),
                    int(self._y1),
                    int(self._x2),
                    int(self._y2),
                )

        self._setCollider()

    def setY(self, y: float):
        """
        Establece la cooordenada y del objeto.

        Args:
            y (float): La coordenada y del objeto.
        """
        if self._y1 == y:
            return

        self._y1 = y
        self._y2 = self._y1 + self._height - 1

        if self._item:
            try:
                self._canvas.coords(self._item, int(self._x1), int(self._y1))
            except tk.TclError:
                self._canvas.coords(
                    self._item,
                    int(self._x1),
                    int(self._y1),
                    int(self._x2),
                    int(self._y2),
                )

        self._setCollider()

    def setPosition(self, x: float, y: float):
        """
        Establece la posición del objeto en el mundo de juego.

        Args:
            x (float): Nueva coordenada x del objeto.
            y (float): Nueva coordenada y del objeto.
        """
        if self._x1 == x and self._y1 == y:
            return

        self._x1 = x
        self._y1 = y
        self._x2 = self._x1 + self._width - 1
        self._y2 = self._y1 + self._height - 1

        if self._item:
            try:
                self._canvas.coords(self._item, int(self._x1), int(self._y1))
            except tk.TclError:
                self._canvas.coords(
                    self._item,
                    int(self._x1),
                    int(self._y1),
                    int(self._x2),
                    int(self._y2),
                )

        self._setCollider()

    def setVisibility(self, visible: bool):
        """
        Cambia visibilidad del objeto

        Args:
            visible (bool): True lo muestra. False lo oculta
        """
        if self._item:
            state = "disabled" if visible else "hidden"
            self._canvas.itemconfig(self._item, state=state)

    def setCollisions(self, enable: bool):
        """
        Habilita o deshabilita participar del procesamiento de colisiones.

        Args:
            enable (bool): True para habilitar, False para deshabilitar.
        """
        self._can_collide = enable

    def setCollider(self, dx1: int, dy1: int, dx2: int, dy2: int):
        """
        Ajusta el colisionador restando de su dimensión los desplazamientos entregados.

        Args:
            dx1 (int): Desplazamiento costado izquierdo.
            dy1 (int): Desplazamiento costado superior.
            dx2 (int): Desplazamiento costado derecho.
            dy2 (int): Desplazamiento costado inferior.
        """
        assert (
            dx1 >= 0 and dy1 >= 0 and dx2 >= 0 and dy2 >= 0
        ), "GameObject.setCollider(): Los valores deben ser mayores o iguales a 0."

        self._dcollider = [int(dx1), int(dy1), int(dx2), int(dy2)]
        self._setCollider()

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
        rx1, ry1, rx2, ry2 = gobj.getCollider()
        x1, y1, x2, y2 = self._collider

        return x1 <= rx2 and rx1 <= x2 and y1 <= ry2 and ry1 <= y2

    def onUpdate(self, dt: float, dt_optimal: float):
        """
        Llamado en cada actualización del juego para el objeto.

        Args:
            dt (float): Tiempo en segundos desde la ultima llamada.
            dt_optimal (float): Tiempo en segundos óptimo desde la última llamada (1/fps).
        """

    def onCollision(self, dt: float, dt_optimal: float, gobj):
        """
        Llamado cuando el objeto colisiona con otro objeto.

        Args:
            dt (float): Tiempo en segundos desde la ultima llamada.
            dt_optimal (float): Tiempo en segundos óptimo desde la última llamada (1/fps).
            gobj (GameObject): Objeto con el que colisiona.
        """

    def delete(self):
        """Elimina el objeto del mundo de juego."""
        self.gw._delGObject(self)

        if self._border:
            self._border.delete()

    # --

    def _kill(self):
        del self._border
        del self._debug

        if self._item:
            self._canvas.delete(self._item)
            self._item = 0

        del self._canvas
        del self.gw

    def _addToGame(self):
        GameObject._counter_ = GameObject._counter_ + 1

        if self._item:
            tag = f"{self._layer:04d}-{GameObject._counter_:06d}"
            self._canvas.itemconfig(self._item, tags=(tag,))

        self.gw._addGObject(self)

        if self._debug:
            from MiniGameEngine.Box import Box

            self._border = Box(
                self._x1,
                self._y1,
                1,
                1,
                self._layer,
                tipo="Debug",
                border=1,
                border_color="red",
            )
            self._setCollider()

    def _setDimension(self, width: int, height: int):
        """
        Modifica tamaño del GameObject.

        Args:
            width (int): Ancho de la caja.
            height (int): Alto de la caja.
        """
        if self._width == width and self._height == height:
            return

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

        self._setCollider()

    def _setCollider(self):
        x1 = self._x1 + self._dcollider[0]
        y1 = self._y1 + self._dcollider[1]
        x2 = self._x2 - self._dcollider[2]
        y2 = self._y2 - self._dcollider[3]

        assert (
            x2 >= x1 and y2 >= y1
        ), "GameObject.setCollider(): Los valores entregados no generan un colisionador válido."

        self._collider = [x1, y1, x2, y2]

        if self._border:
            self._border.setPosition(x1, y1)
            self._border.setDimension(x2 - x1 + 1, y2 - y1 + 1)
