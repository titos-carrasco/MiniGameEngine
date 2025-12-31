from MiniGameEngine.Sprite import Sprite


class Pasto(Sprite):
    def __init__(self, x, y, layer):
        super().__init__(
            x, y, layer=layer, tipo="Pasto", image_path="Recursos/Pasto.png"
        )
