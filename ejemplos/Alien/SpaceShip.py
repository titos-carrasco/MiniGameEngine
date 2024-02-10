import time

from MiniGameEngine.Sprite import Sprite
from Bullet import Bullet


class SpaceShip(Sprite):
    # inicializamos la Nave Espacial
    def __init__(self, x, y):
        super().__init__(
            x, y, layer=1, tipo="SpaceShip", imagePath="Recursos/SpaceShip.png"
        )
        self.lastBullet = 0

    # actualizamos el estado de la Nave Espacial en cada frame
    def onUpdate(self, dt):
        ww = self.getWorldWidth()
        w = self.getWidth()
        x = self.getX()
        y = self.getY()

        # movimiento lateral
        move = False
        if self.isPressed("Left"):
            x = x - 4
            if x < 0:
                x = 0
            self.setX(x)
        elif self.isPressed("Right"):
            x = x + 4
            if x + w > ww:
                x = ww - w
            self.setX(x)

        # disparamos una bala
        if self.isPressed("space"):
            if time.time() - self.lastBullet > 0.3:
                Bullet(x + 21, y - 30)
                self.lastBullet = time.time()
