import time
import random
from Bomb import Bomb
from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator
from MiniGameEngine.Animation import Animation


class Invader(Sprite):
    def __init__(self, x, y, images_path):
        super().__init__(x, y, layer=1, tipo="Invader")

        # receptor de colisiones
        self.setCollisionFlag(self.COLLISION_RECEIVER)

        self.cnt = 0
        self.dx = 4
        self.speed = 0.3

        self.animator = Animator(images_path, self, speed=self.speed)

        self.t = time.time()
        self.last_bomb = time.time()

    # manejamos la actualizacion
    def onUpdate(self, dt, dt_optimal):
        self.animator.next()

        if time.time() - self.t < self.speed:
            return

        x, y = self.getPosition()
        x = x + self.dx
        self.cnt = self.cnt + 1
        if self.cnt == 26:
            self.dx = self.dx * -1
            self.cnt = 0
        self.setPosition(x, y)

        t = time.time()
        if random.randint(0, 50) == 25:
            Bomb(x + self.getWidth() / 2, y + self.getHeight() + 1)
        self.t = t

    # manejamos las colisiones
    def onCollision(self, dt, dt_optimal, gobj):
        if gobj.getTipo() == "Missil":
            self.gw.addPoints(10)
            x, y = self.getPosition()
            self.delete()
            Animation(x - 2, y - 6, "Recursos/Invader-Explosion.png")
