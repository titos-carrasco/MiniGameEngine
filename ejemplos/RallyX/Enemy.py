import random

from MiniGameEngine.Sprite import Sprite


class Enemy(Sprite):
    def __init__(self, x, y, getTargetPosition):
        super().__init__(
            x,
            y,
            layer=2,
            tipo="Enemy",
            image_path="Recursos/RedCar-up.png",
            debug=False,
        )

        # iniciador de colisiones
        self.setCollisionFlag(self.COLLISION_INITIATOR)

        self.speed = 200
        self.speed_x = 0
        self.speed_y = -self.speed

        # para obtenber la posición del auto a perseguir
        self.getTargetPosition = getTargetPosition

    def onUpdate(self, dt, dt_optimal):
        x, y = self.getPosition()

        x = x + self.speed_x * dt_optimal
        y = y + self.speed_y * dt_optimal
        self.setPosition(x, y)

    def onCollision(self, dt, dt_optimal, gobj):
        tipo = gobj.getTipo()

        # chocamos al auto que perseguimos
        if tipo == "Car":
            self.speed_x = 0
            self.speed_y = 0

        # tratamos de perseguirlo
        else:
            # nos devolvemos
            x, y = self.getPosition()
            x = x - self.speed_x * dt_optimal
            y = y - self.speed_y * dt_optimal
            self.setPosition(x, y)

            # necesitamos la posición del auto que perseguimos
            car_pos = self.getTargetPosition()
            if car_pos is None:
                return
            cx, cy = car_pos

            # necesitamos nuestro siguiente movimiento
            n = random.randint(1, 4)
            if n == 1:
                self.speed_x = 0
                self.speed_y = -self.speed
                self.setShape("Recursos/RedCar-up.png")
            elif n == 2:
                self.speed_x = 0
                self.speed_y = self.speed
                self.setShape("Recursos/RedCar-down.png")
            elif n == 3:
                self.speed_x = -self.speed
                self.speed_y = 0
                self.setShape("Recursos/RedCar-left.png")
            elif n == 4:
                self.speed_x = self.speed
                self.speed_y = 0
                self.setShape("Recursos/RedCar-right.png")
