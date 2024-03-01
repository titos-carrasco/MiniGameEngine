from MiniGameEngine.Sprite import Sprite


class Heroe(Sprite):
    def __init__(self, x, y):
        super().__init__(
            x, y, layer=2, tipo="Heroe", image_path="Recursos/Heroe/Right-001.png"
        )

    def onUpdate(self, dt):
        ww = self.getWorldWidth()
        w = self.getWidth()
        x = self.getX()
        y = self.getY()

        # movimiento lateral
        if self.isPressed("Left"):
            x = x - 200*dt
            x = max(x, 0)
            self.setX(x)
        elif self.isPressed("Right"):
            x = x + 200*dt
            if x + w > ww:
                x = ww - w
            self.setX(x)
