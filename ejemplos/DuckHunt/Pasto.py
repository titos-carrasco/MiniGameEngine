import time
from MiniGameEngine import GameObject


class Pasto(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, imagePath="Recursos/Pasto.png", tipo="Pasto", layer=2)
