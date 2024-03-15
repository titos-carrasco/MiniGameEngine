from MiniGameEngine.Box import Box
from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Heroe(Sprite):
    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            layer=2,
            tipo="Heroe",
            image_path="Recursos/Heroe/Idle.png",
            debug=False,
        )
        self.setCollisions(True)

        self.jump_force = 500
        self.gravity = 20
        self.y_velocity = 90            # debe ser mayor que cualquier velocidad en Y de las Bases
        self.dy = self.y_velocity
        self.x_velocity = 250
        self.dx = 0
        self.on_ground = False

        self.shape_idle = "Recursos/Heroe/Idle.png"
        self.anim_left = Animator("Recursos/Heroe/Left-*.png")
        self.anim_right = Animator("Recursos/Heroe/Right-*.png")

    def onUpdate(self, dt, dt_optimal):
        x, y = self.getPosition()
        w, h = self.getDimension()
        ww, hh = self.gw.getWidth(), self.gw.getHeight()

        if self.on_ground:
            # movimiento lateral
            if self.gw.isPressed("Left"):
                self.dx = -self.x_velocity * dt_optimal
            elif self.gw.isPressed("Right"):
                self.dx = self.x_velocity * dt_optimal
            else:
                self.dx = 0

            if self.dx > 0:
                shape = self.anim_right.next()
            elif self.dx < 0:
                shape = self.anim_left.next()
            else:
                shape = self.shape_idle
            if shape:
                self.setShape(shape)

            # solicitud de salto
            if self.gw.isPressed("space"):
                self.dy = -self.jump_force
                self.dx = self.dx * 0.3

        # actualizamos coordenadas
        y = y + self.dy * dt_optimal
        self.dy = self.dy + self.gravity

        x = min(max(0, x + self.dx), ww - w)

        self.setPosition(x, y)
        self.on_ground = False

    def onCollision(self, dt, dt_optimal, gobj):
        x, y = self.getPosition()
        w, h = self.getDimension()

        gx, gy = gobj.getPosition()
        gw, gh = gobj.getDimension()
        tipo = gobj.getTipo()

        if tipo == "Suelo":
            if self.y_velocity >= 0:
                self.setY(gy - h)
                self.dy = self.y_velocity
                self.on_ground = True

        elif tipo == "Muro":
            if x > gx:
                self.setX(gx + gw)
            else:
                self.setX(gx - w)
