import math
from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Pacman(Sprite):
    def __init__(self, x, y, layer):
        super().__init__(x, y, layer=layer, tipo="Pacman")

        # para el movimiento
        self.speed = 200
        self.last_x = x
        self.last_y = y
        self.mult = 4
        self.stop = 16
        self.moving = "-"

        # iniciador de colisiones
        self.setCollisionFlag(self.COLLISION_INITIATOR)

        self.animator = Animator("Recursos/Pacman-L*.png", self, speed=0.6)
        self.animator.start()

    # actualizamos su estado en cada frame
    def onUpdate(self, dt, _dt_optimal):
        self.animator.next()
        x, y = self.getPosition()
        self.last_x = x
        self.last_y = y

        if self.gw.isPressed("Left"):
            x = round(x - self.speed * dt)
            x = math.floor(x / self.mult) * self.mult
            self.moving = "L"
            self.setX(x)
        elif self.gw.isPressed("Right"):
            x = x + self.speed * dt
            x = math.ceil(x / self.mult) * self.mult
            self.moving = "R"
            self.setX(x)
        elif self.gw.isPressed("Up"):
            y = y - self.speed * dt
            y = math.floor(y / self.mult) * self.mult
            self.moving = "U"
            self.setY(y)
        elif self.gw.isPressed("Down"):
            y = y + self.speed * dt
            y = math.ceil(y / self.mult) * self.mult
            self.moving = "D"
            self.setY(y)
        else:
            if self.moving != "-":
                if self.moving == "L":
                    x = math.floor(x / self.stop) * self.stop
                    self.setX(x)
                elif self.moving == "R":
                    x = math.ceil(x / self.stop) * self.stop
                    self.setX(x)
                elif self.moving == "U":
                    y = math.floor(y / self.stop) * self.stop
                    self.setY(y)
                elif self.moving == "D":
                    y = math.ceil(y / self.stop) * self.stop
                    self.setY(y)
                self.moving = "-"

        self.setPosition(x, y)

    def onCollision(self, _dt, _dt_optimal, gobj):
        x, y = self.getPosition()
        if gobj.getTipo() == "Bloque":
            if x != self.last_x:
                self.setX(self.last_x)
            if y != self.last_y:
                self.setY(self.last_y)
            print("Bloque")
