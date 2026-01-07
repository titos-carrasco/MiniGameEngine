import time
import random
from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Inky(Sprite):
    def __init__(self, x, y, layer):
        super().__init__(x, y, layer=layer, tipo="Ghost")

        self.setCollisionFlag(self.COLLISION_INITIATOR)

        self.animLeft = Animator("./Recursos/Inky/L*", self, speed=0.4)
        self.animRight = Animator("./Recursos/Inky/R*", self, speed=0.4)
        self.animUp = Animator("./Recursos/Inky/U*", self, speed=0.4)
        self.animDown = Animator("./Recursos/Inky/D*", self, speed=0.4)
        self.animator = self.animDown
        self.animator.start()

        self.moving = "L"
        self.speed = 50
        self.inJail = 2
        self.time = time.time()

    def onUpdate(self, dt, _dt_optimal):
        self.animator.next()
        x, y = self.getPosition()

        # pausa inicial
        if self.inJail == 2:
            if time.time() - self.time > 2:
                self.inJail = 1
            return

        elif self.inJail == 1:
            if x < 208:
                x = round(x + self.speed * dt)
                self.setX(x)
                return
            if y > 224:
                y = round(y - self.speed * dt)
                self.setY(y)
                return
            self.inJail = 0

        self.last_x = x
        self.last_y = y

        if self.moving == "L":
            self.setX(round(x - self.speed * dt))
        elif self.moving == "R":
            self.setX(round(x + self.speed * dt))
        elif self.moving == "U":
            self.setY(round(y - self.speed * dt))
        elif self.moving == "D":
            self.setY(round(y + self.speed * dt))

    def onCollision(self, _dt, _dt_optimal, gobj):
        if self.inJail != 0:
            return
        x, y = self.getPosition()
        if gobj.getTipo() == "Muro":
            if x != self.last_x:
                self.setX(self.last_x)
            if y != self.last_y:
                self.setY(self.last_y)
            self.moving = random.choice(["U", "D", "L", "R"])
