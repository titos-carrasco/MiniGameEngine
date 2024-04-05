import time

from Smoke import Smoke
from MiniGameEngine.Sprite import Sprite


class Car(Sprite):
    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            layer=2,
            tipo="Car",
            image_path="Recursos/BlueCar-up.png",
            debug=False,
        )

        # iniciador y receptor de colisiones
        self.setCollisionFlag(self.COLLISION_INITIATOR + self.COLLISION_RECEIVER)

        self.last_smoke = 0

        self.speed = 200
        self.speed_x = 0
        self.speed_y = -self.speed

    def onUpdate(self, dt, dt_optimal):
        x, y = self.getPosition()

        if self.gw.isPressed("Up"):
            self.speed_x = 0
            self.speed_y = -self.speed
            self.setShape("Recursos/BlueCar-up.png")
        elif self.gw.isPressed("Down"):
            self.speed_x = 0
            self.speed_y = self.speed
            self.setShape("Recursos/BlueCar-down.png")
        if self.gw.isPressed("Left"):
            self.speed_x = -self.speed
            self.speed_y = 0
            self.setShape("Recursos/BlueCar-left.png")
        elif self.gw.isPressed("Right"):
            self.speed_x = self.speed
            self.speed_y = 0
            self.setShape("Recursos/BlueCar-right.png")

        if self.gw.isPressed("space"):
            if time.time() - self.last_smoke > 0.5:
                Smoke(x - 4, y - 4)
                self.last_smoke = time.time()

        x = x + self.speed_x * dt_optimal
        y = y + self.speed_y * dt_optimal
        self.setPosition(x, y)

    def onCollision(self, dt, dt_optimal, gobj):
        tipo = gobj.getTipo()
        if tipo == "Muro":
            x, y = self.getPosition()
            x = x - self.speed_x * dt_optimal * 1.5
            y = y - self.speed_y * dt_optimal * 1.5
            self.setPosition(x, y)

        elif tipo == "Enemy":
            pass
