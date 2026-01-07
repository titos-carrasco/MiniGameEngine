import math
from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Pacman(Sprite):
    def __init__(self, x, y, layer, game):
        super().__init__(
            x, y, layer=layer, tipo="Pacman", image_path="./Recursos/Pacman/Left-0.png"
        )

        # para interactuar con el controlador del juego
        self.game = game

        # para el movimiento
        self.speed = 1
        self.last_x = x
        self.last_y = y
        self.moving = "-"

        # iniciador de colisiones
        self.setCollisionFlag(self.COLLISION_INITIATOR + self.COLLISION_RECEIVER)

        # las animaciones
        self.animator = None
        self.animLeft = Animator("Recursos/Pacman/Left*.png", self, speed=0.1)
        self.animRight = Animator("Recursos/Pacman/Right*.png", self, speed=0.1)
        self.animUp = Animator("Recursos/Pacman/Up*.png", self, speed=0.1)
        self.animDown = Animator("Recursos/Pacman/Down*.png", self, speed=0.1)
        self.animDead = Animator(
            "Recursos/Pacman/Die*.png", self, speed=0.1, repeat=False
        )

    # actualizamos su estado en cada frame
    def onUpdate(self, _dt, _dt_optimal):
        if self.animator:
            self.animator.next()

        if self.moving == "Dead":
            return

        x, y = self.getPosition()
        self.last_x = x
        self.last_y = y

        if x >= 460:
            x = -28
        elif x <= -28:
            x = 460

        if self.gw.isPressed("Left"):
            x = x - self.speed
            self.setX(x)
            if self.moving != "L":
                self.animator = self.animLeft
                self.animator.start()
                self.moving = "L"
        elif self.gw.isPressed("Right"):
            x = x + self.speed
            self.setX(x)
            if self.moving != "R":
                self.animator = self.animRight
                self.animator.start()
                self.moving = "R"
        elif self.gw.isPressed("Up"):
            y = y - self.speed
            self.setY(y)
            if self.moving != "U":
                self.animator = self.animUp
                self.animator.start()
                self.moving = "U"
        elif self.gw.isPressed("Down"):
            y = y + self.speed
            self.setY(y)
            if self.moving != "D":
                self.animator = self.animDown
                self.animDown.start()
                self.moving = "D"
        else:
            if self.moving != "-":
                self.animator.stop()
                self.animator = None
                self.setShape("./Recursos/Pacman/Left-0.png")
                if self.moving == "L":
                    x = x // 8 * 8
                    self.setX(x)
                elif self.moving == "R":
                    x = (x + 8) // 8 * 8
                    self.setX(x)
                elif self.moving == "U":
                    y = y // 8 * 8
                    self.setY(y)
                elif self.moving == "D":
                    y = (y + 8) // 8 * 8
                    self.setY(y)
                self.moving = "-"

        self.setPosition(x, y)

    def onCollision(self, _dt, _dt_optimal, gobj):
        if self.moving == "Dead":
            return

        x, y = self.getPosition()
        if gobj.getTipo() == "Muro":
            if x != self.last_x:
                self.setX(self.last_x)
            if y != self.last_y:
                self.setY(self.last_y)
        elif gobj.getTipo() == "Punto":
            w, h = self.getDimension()
            x = x + w / 2
            y = y + h / 2
            xp, yp = gobj.getPosition()
            w, h = gobj.getDimension()
            xp = xp + w / 2
            yp = yp + h / 2
            d = abs(math.hypot(xp - x, yp - y))
            if d <= 8:
                gobj.delete()
                self.game.eatDot()
        elif gobj.getTipo() == "Circulo":
            w, h = self.getDimension()
            x = x + w / 2
            y = y + h / 2
            xp, yp = gobj.getPosition()
            w, h = gobj.getDimension()
            xp = xp + w / 2
            yp = yp + h / 2
            d = abs(math.hypot(xp - x, yp - y))
            if d <= 12:
                gobj.delete()
                self.game.eatCircle()

        elif gobj.getTipo() == "Ghost":
            w, h = self.getDimension()
            x = x + w / 2
            y = y + h / 2
            xp, yp = gobj.getPosition()
            w, h = gobj.getDimension()
            xp = xp + w / 2
            yp = yp + h / 2
            d = abs(math.hypot(xp - x, yp - y))
            if d <= 30:
                self.moving = "Dead"
                self.animator = self.animDead
                self.animator.start()
