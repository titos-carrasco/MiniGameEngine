from MiniGameEngine.Sprite import Sprite


class Rana(Sprite):
    # inicializamos el objeto
    def __init__(self, x, y, layer, speed):
        super().__init__(
            x,
            y,
            layer=layer,
            tipo="Rana",
            image_path=f"Recursos/Rana-001.png",
        )

        # receptor de colisiones
        self.setCollisionFlag(self.COLLISION_INITIATOR)

        self.speed = speed

    def onUpdate(self, dt, dt_optimal):
        x, y = self.getPosition()

        if self.gw.isPressed("Left"):
            x = x - self.speed * dt
            if x < 0:
                x = 0
            self.setX(x)
        elif self.gw.isPressed("Right"):
            x = x + self.speed * dt
            if x > self.gw.getWidth() - self.getWidth():
                x = self.gw.getWidth() - self.getWidth()
            self.setX(x)
