class Camera:
    """
    Clase que representa una cámara utilizada para desplegar el mundo del juego
    """

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        world_width: int,
        world_height: int,
    ):
        """
        Crea un objeto del tipo "Camera".
        Es creada internamente al crear una instancia del GameWorld

        Args:
            x (int): Coordenada x de la posición de la cámara
            y (int): Coordenada y de la posición de la cámara
            width (int): Ancho de la cámara
            height (int): Alto de la cámara
            world_width (int): Ancho del mundo del juego
            world_height (int): Alto del mundo del juego
        """
        width, height = int(width), int(height)
        assert width > 0, "Camera(): width debe ser mayor que 0."
        assert height > 0, "Camera(): height debe ser mayor que 0."

        world_width, world_height = int(world_width), int(world_height)
        assert (
            world_width >= width
        ), "Camera(): world_width debe ser mayor o igual que width."
        assert (
            world_width >= width
        ), "Camera(): world_width debe ser mayor o igual que width."

        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._world_width = world_width
        self._world_height = world_height

        self._target = None
        self._gobjects = {}

    def setTarget(self, gobj):
        """Establece el Game Object que será seguido por la Cámara

        Args:
            target (GameObject): GameObject a seguri y centrar en la ventana del mundo
        """
        self._target = gobj

    def addGameObject(self, gobj):
        """
        Agrega un GameObject dentro de la zona de la cámara.
        Las coordenadas iniciales del objeto son utilizadas dentro de la cámara

        Args:
            gobj (GameObject): El GameObject a agregar
        """
        if not gobj in self._gobjects:
            x, y = gobj.getPosition()
            self._gobjects[gobj] = x, y
            gobj.setPosition(self._x + x, self._y + y)

    def delGameObject(self, gobj):
        """
        Elimina un GameObject de la zona de la cámara.

        Args:
            gobj (GameObject): El GameObject a eliminar
        """
        if gobj in self._gobjects:
            del self._gobjects[gobj]

    def setPosition(self, x: int, y: int):
        """
        Posiciona la cámara en el mundo del juego

        Args:
            x (int): Posición x de la cámara
            y (int): Posición y de la cámara
        """
        self._x, self._y = int(x), int(y)

        for item in self._gobjects.items():
            gobj, (ox, oy) = item
            gobj.setPosition(x + ox, y + oy)

    def moveToTarget(self):
        """
        Desplaza la cámara hacia su target dejándolo en el centro de ella.
        """
        if self._target is None:
            return 0, 0

        xt, yt = self._target.getPosition()
        wt, ht = self._target.getDimension()

        x = xt + wt / 2 - self._width / 2
        y = yt + ht / 2 - self._height / 2

        if x < 0:
            x = 0
        elif x + self._width >= self._world_width:
            x = self._world_width - self._width

        if y < 0:
            y = 0
        elif y + self._height >= self._world_height:
            y = self._world_height - self._height

        self.setPosition(x, y)

        return self._x, self._y
