import time

from Bullet import Bullet
from Animation import Animation

from MiniGameEngine.Sprite import Sprite


class SpaceShip(Sprite):
    # inicializamos la Nave Espacial
    def __init__(self, x, y):
        super().__init__(
            x, y, layer=2, tipo="SpaceShip", image_path="Recursos/SpaceShip.png"
        )

        # receptor de colisiones
        self.setCollisionFlag(self.COLLISION_RECEIVER)

        # instante en que se lanzó la última bala
        self.last_bullet = 0

        # El juego continua mientras estoy vivo
        self.alive = True

    # actualizamos el estado de la Nave Espacial en cada frame
    def onUpdate(self, dt, dt_optimal):
        ww = self.gw.getWidth()
        w = self.getWidth()
        x = self.getX()
        y = self.getY()

        # movimiento lateral
        if self.gw.isPressed("Left"):
            x = x - 200 * dt_optimal
            x = max(x, 10)
            self.setX(x)
        elif self.gw.isPressed("Right"):
            x = x + 200 * dt_optimal
            if x + w + 20 > ww:
                x = ww - w - 20
            self.setX(x)

        # disparamos una bala
        if self.gw.isPressed("space"):
            if time.time() - self.last_bullet > 0.3:
                Bullet(x + 12, y - 6)
                self.last_bullet = time.time()

    # manejamos las colisiones
    def onCollision(self, dt, dt_optimal, gobj):
        x, y = self.getPosition()
        self.delete()
        self.alive = False

        Animation(
            x - 24, y - 24, "Recursos/SpaceShipExplosion-*.png", speed=0.1, duration=0.4
        )

    def isAlive(self):
        return self.alive
