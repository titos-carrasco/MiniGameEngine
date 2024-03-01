import time

from MiniGameEngine.Sprite import Sprite


class Mundo(Sprite):
    def __init__(self):
        super().__init__(
            0, 0, layer=1, tipo="Mundo", image_path="
        )

    def onUpdate(self, dt):
        pass
