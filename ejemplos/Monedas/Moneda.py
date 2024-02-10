from MiniGameEngine.Sprite import Sprite


class Moneda(Sprite):
    # inicializamos la Moneda
    def __init__(self, x, y, layer):
        super().__init__(
            x, y, layer=layer, tipo="Moneda", imagePath="Recursos/Moneda.png"
        )
        self.setCollisions(True)
