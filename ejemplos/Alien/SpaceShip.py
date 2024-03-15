import time

from Bullet import Bullet
from MiniGameEngine.Sprite import Sprite


class SpaceShip(Sprite):
    # inicializamos la Nave Espacial
    def __init__(self, x, y):
        super().__init__(
            x, y, layer=1, tipo="SpaceShip", image_path="Recursos/SpaceShip.png"
        )
        # instante en que se lanzó la última bala
        self.last_bullet = 0

    # actualizamos el estado de la Nave Espacial en cada frame
    def onUpdate(self, dt, dt_optimal):
        ww = self.gw.getWidth()
        w = self.getWidth()
        x = self.getX()
        y = self.getY()

        # movimiento lateral
        if self.gw.isPressed("Left"):
            x = x - 200 * dt_optimal
            x = max(x, 0)
            self.setX(x)
        elif self.gw.isPressed("Right"):
            x = x + 200 * dt_optimal
            if x + w > ww:
                x = ww - w
            self.setX(x)

        # disparamos una bala
        if self.gw.isPressed("space"):
            if time.time() - self.last_bullet > 0.3:
                Bullet(x + 21, y - 30)
                self.last_bullet = time.time()
