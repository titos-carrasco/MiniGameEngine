from MiniGameEngine.GameObject import GameObject


class Sprite(GameObject):
    """Clase que representa un GameObject definido por una imagen."""

    def __init__(
        self,
        x: float,
        y: float,
        layer: int,
        tipo: str,
        image_path: str,
        debug: bool = False,
    ):
        """
        Crea un objeto de la clase Sprite.

        Args:
            x (float): Coordenada x del sprite.
            y (float): Coordenada y del sprite.
            layer (int): Capa en que se colocará este sprite.
            tipo (str): Tipo de sprite.
            image_path (str): Archivo con la imagen del sprite.
            debug (bool, opcional): True para mostrar información del sprite.
        """
        super().__init__(x, y, width=1, height=1, layer=layer, tipo=tipo, debug=debug)

        # creamos la imagen
        self._item = self._canvas.create_image(
            int(x),
            int(y),
            anchor="nw",
            state="disabled",
        )

        # cargamos la imagen
        self._image = None
        self.setShape(image_path)

        # lo agregamos al juego
        self._addToGame()

    def setShape(self, image_path: str):
        """
        Cambia la imagen del sprite.

        Args:
            imagePath (str): Archivo con la nueva imagen para el sprite.
        """
        img = self.gw.loadImage(image_path)
        if img != self._image:
            self._canvas.itemconfig(self._item, image=img)
            width, height = img.width(), img.height()
            self._setDimension(width, height)
            self._image = img
