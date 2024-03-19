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
        self.dc = 4
        self.setCollider(self.dc, 0, self.dc, 0)
        self.setCollisions(True)

        self.jump_force = 500
        self.gravity = 20
        self.velocity_y = 90  # debe ser mayor que cualquier velocidad en Y de las Bases
        self.dy = self.velocity_y
        self.velocity_x = 250
        self.dx = 0
        self.on_ground = False
        self.on_stairs = False

        self.shape_idle = "Recursos/Heroe/Idle.png"
        self.anim_left = Animator("Recursos/Heroe/Left-*.png")
        self.anim_right = Animator("Recursos/Heroe/Right-*.png")

    def onUpdate(self, dt, dt_optimal):
        x, y = self.getPosition()
        w, _ = self.getDimension()
        ww, _ = self.gw.getWidth(), self.gw.getHeight()

        if self.on_stairs or self.on_ground:
            # movimiento vertical
            if self.on_stairs:
                if self.gw.isPressed("Up"):
                    self.dy = -self.velocity_y
                elif self.gw.isPressed("Down"):
                    self.dy = self.velocity_y
                else:
                    self.dy = 0

            # movimiento lateral
            if self.gw.isPressed("Left"):
                self.dx = -self.velocity_x * dt_optimal
            elif self.gw.isPressed("Right"):
                self.dx = self.velocity_x * dt_optimal
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
            if self.on_ground and self.gw.isPressed("space"):
                self.dy = -self.jump_force
                self.dx = self.dx * 0.8

        # actualizamos coordenadas
        y = y + self.dy * dt_optimal
        self.dy = self.dy + self.gravity

        x = min(max(0, x + self.dx), ww - w)

        self.setPosition(x, y)
        self.on_ground = False
        self.on_stairs = False

    def onCollision(self, dt, dt_optimal, gobj):
        x, y = self.getPosition()
        w, h = self.getDimension()

        gx, gy = gobj.getPosition()
        gw, _ = gobj.getDimension()
        tipo = gobj.getTipo()

        if tipo == "Suelo" or tipo == "Base":
            # solo si viene cayendo y el 40% inferior colisionó
            if self.dy > 0 and y + h - 1 - gy < h * 0.4:
                self.setY(gy - h)
                self.dy = self.velocity_y
                self.on_ground = True

            if tipo == "Base":
                dx, _ = gobj.getDisplacement()
                self.setX(x - dx)

        elif tipo == "Escalera":
            self.on_stairs = True

        elif tipo == "Muro":
            if x > gx:
                self.setX(gx + gw - self.dc)
            else:
                self.setX(gx - w + self.dc)
