from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Box import Box


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

        self.box = Box(
            1,
            1,
            width=10,
            height=10,
            layer=5,
            tipo=None,
            line_width=1,
            line_color="yellow",
            fill_color="yellow",
        )
        self.box.setVisibility(False)

        self.vy = 0
        self.fy = -300
        self.g = 800

        self.last_position = self.getPosition()

    def onUpdate(self, dt):
        x, y = self.getPosition()
        ww = self.gw.getWidth()
        w = self.getWidth()

        self.box.setVisibility(False)
        self.last_position = x, y

        # movimiento lateral
        if self.gw.isPressed("Left"):
            x = x - 200 * dt
            x = max(x, 0)
            self.setX(x)
        if self.gw.isPressed("Right"):
            x = x + 200 * dt
            x = min(x, ww - w)
            self.setX(x)

        # movimiento vertical
        if self.gw.isPressed("space"):
            self.vy = self.fy

        y = y + self.vy * dt
        self.vy = self.vy + self.g * dt
        self.setY(y)

    def onCollision(self, dt, gobj):
        #r1 = self.getRectangle()
        #r2 = gobj.getRectangle()
        # r = r1.intersection(r2)

        # self.box.setPosition(r.getX(), r.getY())
        # self.box.setDimension(r.getWidth(), r.getHeight())
        self.box.setVisibility(True)

        x, y = self.getPosition()
        h = self.getHeight()
        tipo = gobj.getTipo()

        if tipo == "Suelo":
            oy = gobj.getY()
            dy = y + h - 1 - oy
            if dy >= 0 and dy <= 10000:
                y = oy - h
                self.setY(y)
                self.vy = 0
        elif tipo == "Muro":
            x, y = self.last_position
            self.setPosition(x, y)
