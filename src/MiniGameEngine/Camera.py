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
        self._x = int(x)
        self._y = int(y)
        self._width = int(width)
        self._height = int(height)
        self._world_width = int(world_width)
        self._world_height = int(world_height)

        self._target = None
        self._gobjects = {}

    def getX(self) -> int:
        """
        Retorna la posición x de la cámara

        Returns:
            int: La posición x de la cámara
        """
        return self._x

    def getY(self) -> int:
        """
        Retorna la posición y de la cámara

        Returns:
            int: La posición y de la cámara
        """
        return self._y

    def getPosition(self) -> (int, int):
        """
        Retorna la posición x e y de la cámara

        Returns:
            int, int: La posición x e y de la cámara
        """
        return self._x, self._y

    def getWidth(self) -> int:
        """
        Retorna el ancho de la cámara

        Returns:
            int: El ancho de la cámara
        """
        return self._width

    def getHeight(self) -> int:
        """
        Retorna el alto de la cámara

        Returns:
            int: El alto de la cámara
        """
        return self._height

    def getDimension(self) -> (int, int):
        """
        Retorna el ancho y alto de la cámara

        Returns:
            int, int: El ancho y alto de la cámara
        """
        return self._width, self._height

    def setPosition(self, x: int, y: int):
        """
        Posiciona la cámara en el mundo del juego

        Args:
            x (int): Posición x de la cámara
            y (int): Posición y de la cámara
        """
        x, y = int(x), int(y)
        self._x, self._y = x, y

        for gobj in self._gobjects:
            ox, oy = self._gobjects[gobj]
            gobj.setPosition(x + ox, y + oy)

    def setTarget(self, target):
        """Establece el Game Object que será seguido por la Cámara

        Args:
            target (GameObject): GameObject a seguri y centrar en la ventana del mundo
        """
        self._target = target

    def addGameObject(self, gobj):
        """
        Agrega un GameObject dentro de la zona de la cámara

        Args:
            gobj (GameObject): El GameObject a agregar
        """
        if not gobj in self._gobjects:
            x, y = gobj.getPosition()
            self._gobjects[gobj] = x, y
            gobj.setPosition(self._x + x, self._y + y)

    # ---

    def _delGameObject(self, gobj):
        if gobj in self._gobjects:
            del self._gobjects[gobj]

    # coloca el GameObject al centro de la cámara
    def _followTarget(self):
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
        x = x

        if y < 0:
            y = 0
        elif y + self._height >= self._world_height:
            y = self._world_height - self._height
        y = y

        self.setPosition(x, y)

        return self._x, self._y
