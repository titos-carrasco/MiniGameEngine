from MiniGameEngine.Sprite import Sprite


class Pasto(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, layer=2, tipo="Pasto", image_path="Recursos/Pasto.png")
