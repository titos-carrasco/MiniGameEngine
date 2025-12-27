from MiniGameEngine.Animator import Animator
from MiniGameEngine.Sprite import Sprite


class Rana(Sprite):
    # inicializamos el objeto
    def __init__(self, x, y, layer, speed):
        super().__init__(
            x,
            y,
            layer=layer,
            tipo="Rana",
            image_path="Recursos/RanaU-001.png",
        )

        # receptor de colisiones
        self.setCollisionFlag(self.COLLISION_INITIATOR)

        self.ymax = y
        self.speed = speed
        self.moving = "-"
        self.animator_up = Animator("Recursos/RanaU*.png", self)
        self.animator_down = Animator("Recursos/RanaD*.png", self)
        self.animator_left = Animator("Recursos/RanaL*.png", self)
        self.animator_right = Animator("Recursos/RanaR*.png", self)
        self.animator_idle = Animator("Recursos/RanaU-001.png", self)
        self.animator = self.animator_idle

    def onUpdate(self, dt, dt_optimal):
        x, y = self.getPosition()

        if self.gw.isPressed("Up"):
            if self.moving != "U":
                self.moving = "U"
                self.animator = self.animator_up
            y = y - self.speed * dt
            self.setY(y)
        elif self.gw.isPressed("Down"):
            if self.moving != "D":
                self.moving = "D"
                self.animator = self.animator_down
            y = y + self.speed * dt
            if y > self.ymax:
                y = self.ymax
            self.setY(y)
        elif self.gw.isPressed("Left"):
            if self.moving != "L":
                self.moving = "L"
                self.animator = self.animator_left
            x = max(x - self.speed * dt, 0)
            self.setX(x)
        elif self.gw.isPressed("Right"):
            if self.moving != "R":
                self.moving = "R"
                self.animator = self.animator_right
            x = x + self.speed * dt
            if x > self.gw.getWidth() - self.getWidth():
                x = self.gw.getWidth() - self.getWidth()
            self.setX(x)
        elif self.moving != "-":
            self.moving = "-"
            self.animator = self.animator_idle

        self.animator.next()
