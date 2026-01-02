import time
from MiniGameEngine.Sprite import Sprite


class Smoke(Sprite):
    def __init__(self, x, y, layer):
        super().__init__(
            x, y, layer=layer, tipo="Smoke", image_path="Recursos/Smoke.png"
        )

        self.t = time.time()

    def onUpdate(self, _dt, _dt_optimal):
        if time.time() - self.t > 1:
            self.delete()
