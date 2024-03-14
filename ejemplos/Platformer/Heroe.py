from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Box import Box
import time


class Heroe(Sprite):
    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            layer=2,
            tipo="Heroe",
            image_path="Recursos/Heroe/Right-001.png",
            debug=True,
        )
        self.setCollisions(True)

        self.box = Box(0, 0, 1, 1, 2, "", 0, None, "yellow")

        self.JUMP_FORCE = 300
        self.GRAVITY = 10
        self.yVelocity = 300
        self.xVelocity = 300

    def onUpdate(self, dt):
        x, y = self.getPosition()
        w, h = self.getDimension()
        ww, hh = self.gw.getWidth(), self.gw.getHeight()

        self.box.setVisibility(False)

        # movimiento lateral
        if self.gw.isPressed("Left"):
            x = x - self.xVelocity * dt
            if x < 0:
                x = 0
            self.setX(x)
        elif self.gw.isPressed("Right"):
            x = x + self.xVelocity * dt
            if x + w >= ww:
                x = ww - w
            self.setX(x)

        # movimiento vertical
        if self.gw.isPressed("space"):
            self.yVelocity = -self.JUMP_FORCE

        y = y + self.yVelocity * dt
        self.setY(y)
        self.yVelocity = self.yVelocity + self.GRAVITY

    def onCollision(self, dt, gobj):
        tipo = gobj.getTipo()
        rx, ry, rw, rh = self.intersection(gobj)
        self.box.setPosition(rx, ry)
        self.box.setDimension(rw, rh)
        self.box.setVisibility(True)

        x, y = self.getPosition()
        w, h = self.getDimension()

        gx, gy = gobj.getPosition()
        gw, gh = gobj.getDimension()

        if tipo == "Suelo":
            if y + h > gy:
                self.setY(gy - h)
                self.yVelocity = 0

        elif tipo == "Muro":
            if x > gx:
                self.setX(gx + gw)
            else:
                self.setX(gx - w)
