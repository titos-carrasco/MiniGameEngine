from MiniGameEngine.Sprite import Sprite


class Vehiculo(Sprite):
    # inicializamos el objeto
    def __init__(self, x, y, layer, skin, direccion, speed):
        super().__init__(
            x,
            y,
            layer=layer,
            tipo="Vehiculo",
            image_path=f"Recursos/{skin}-{direccion}.png",
        )

        # receptor de colisiones
        self.setCollisionFlag(self.COLLISION_RECEIVER)

        self.dir = 1 if direccion == "R" else -1
        self.speed = speed

    def onUpdate(self, dt, dt_optimal):
        x = self.getX()
        x = x + self.speed * self.dir * dt

        if self.dir > 0 and x > self.gw.getWidth():
            x = -160
        elif self.dir < 0 and x < -160:
            x = self.gw.getWidth()

        self.setX(x)
