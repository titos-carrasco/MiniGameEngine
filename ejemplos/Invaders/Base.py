import time

from Missil import Missil
from MiniGameEngine.Sprite import Sprite


class Base(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, layer=1, tipo="Base", image_path="Recursos/Base.png")

        # receptor de colisiones
        self.setCollisionFlag(self.COLLISION_RECEIVER)

        # instante en que se lanzó el último misil
        self.last_missil = 0

    # actualizamos su estado en cada frame
    def onUpdate(self, dt, dt_optimal):
        x, y = self.getPosition()

        # movimiento lateral
        if self.gw.isPressed("Left"):
            x = x - 200 * dt_optimal
            x = max(x, 70)
            self.setX(x)
        elif self.gw.isPressed("Right"):
            x = x + 200 * dt_optimal
            if x > 520:
                x = 520
            self.setX(x)

        # disparamos un misil
        if self.gw.isPressed("space"):
            if time.time() - self.last_missil > 0.3:
                Missil(x + 12, y - 14)
                self.last_missil = time.time()
