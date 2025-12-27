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

        self.speed = speed
        self.dir = "U"
        self.animator = Animator("Recursos/RanaU*.png", repeat=False)

    def onUpdate(self, dt, dt_optimal):
        x, y = self.getPosition()

        if self.gw.isPressed("Up"):
            if self.dir != "U":
                self.dir = "U"
                self.animator = Animator("Recursos/RanaU*.png", repeat=False)
        elif self.gw.isPressed("Down"):
            if self.dir != "D":
                self.dir = "D"
                self.animator = Animator("Recursos/RanaD*.png", repeat=False)
        elif self.gw.isPressed("Left"):
            if self.dir != "L":
                self.dir = "L"
                self.animator = Animator("Recursos/RanaL*.png", repeat=False)
            x = max(x - self.speed * dt, 0)
            self.setX(x)
        elif self.gw.isPressed("Right"):
            if self.dir != "R":
                self.dir = "E"
                self.animator = Animator("Recursos/RanaR*.png", repeat=False)
            x = x + self.speed * dt
            if x > self.gw.getWidth() - self.getWidth():
                x = self.gw.getWidth() - self.getWidth()
            self.setX(x)

        img = self.animator.next()
        if img:
            self.setShape(img)
