from MiniGameEngine.GameObject import GameObject


class EmptyObject(GameObject):
    """Clase que representa un GameObject vacio."""

    def __init__(
        self,
        x: float,
        y: float,
        width: int,
        height: int,
        layer: int,
        tipo: str = None,
        debug: bool = False,
    ):
        """
        Crea una un objeto de la clase EmptyObject.

        Args:
            x (float): Coordenada x del texto.
            y (float): Coordenada y del texto.
            width (int): Ancho de la caja.
            height (int): Alto de la caja.
            layer (int): Capa en que se colocará este texto.
            tipo (str, opcional): Tipo de texto.
            debug (bool, opcional): True para mostrar información del texto.
        """
        super().__init__(x, y, width, height, layer=layer, tipo=tipo, debug=debug)

        # lo agregamos al juego
        self._addToGame()
