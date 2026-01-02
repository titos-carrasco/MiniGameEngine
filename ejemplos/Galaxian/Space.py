import time
from MiniGameEngine.Sprite import Sprite


class Space(Sprite):
    def __init__(self, layer):
        super().__init__(
            0, -600, layer=layer, tipo="Space", image_path="Recursos/Space.png"
        )
        self.t = time.time()

    def onUpdate(self, _dt, dt_optimal):
        if time.time() - self.t < 0.03:
            return
        y = self.getY() + 100 * dt_optimal
        if y >= 0:
            y = -600
        self.setY(y)
        self.t = time.time()
