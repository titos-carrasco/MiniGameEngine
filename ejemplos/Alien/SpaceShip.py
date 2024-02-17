import time

from Bullet import Bullet
from MiniGameEngine.Sprite import Sprite


class SpaceShip(Sprite):
    # inicializamos la Nave Espacial
    def __init__(self, x, y):
        super().__init__(
            x, y, layer=1, tipo="SpaceShip", image_path="Recursos/SpaceShip.png"
        )
        self.last_bullet = 0

    # actualizamos el estado de la Nave Espacial en cada frame
    def onUpdate(self, dt):
        ww = self.getWorldWidth()
        w = self.getWidth()
        x = self.getX()
        y = self.getY()

        # movimiento lateral
        if self.isPressed("Left"):
            x = x - 4
            x = max(x, 0)
            self.setX(x)
        elif self.isPressed("Right"):
            x = x + 4
            if x + w > ww:
                x = ww - w
            self.setX(x)

        # disparamos una bala
        if self.isPressed("space"):
            if time.time() - self.last_bullet > 0.3:
                Bullet(x + 21, y - 30)
                self.last_bullet = time.time()
