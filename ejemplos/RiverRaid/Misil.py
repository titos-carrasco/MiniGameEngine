import time
from MiniGameEngine.Sprite import Sprite


class Misil(Sprite):
    def __init__(self, x, y, layer):
        super().__init__(
            x, y, layer=layer, tipo="Misil", image_path="./Recursos/Misil.png"
        )

        self.setCollisionFlag(self.COLLISION_INITIATOR)
        self.start = time.time()

    def onUpdate(self, dt, _dt_optimal):
        if(time.time() - self.start > 2):
            self.delete()
        else:
            y = self.getY()
            y = y - 300 * dt
            self.setY(y)

    def onCollision(self, _dt, _dt_optimal, gobj):
        self.delete()
