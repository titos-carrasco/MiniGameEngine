import time
from Misil import Misil
from Explosion import Explosion
from MiniGameEngine.Sprite import Sprite


class Avion(Sprite):
    # inicializamos la Nave Espacial
    def __init__(self, x, y, layer, speed):
        super().__init__(
            x, y, layer=layer, tipo="Avion", image_path="Recursos/Avion-C.png"
        )
        self.setCollisionFlag(self.COLLISION_INITIATOR + self.COLLISION_RECEIVER)

        self.speed = speed
        self.init_x = x
        self.init_y = y

        self.moving = "C"
        self.running = False
        self.last_missil = time.time()

    def start(self):
        self.setPosition(self.init_x, self.init_y)
        self.running = True

    def stop(self):
        self.setShape("./Recursos/Avion-C.png")
        self.moving = "C"
        self.running = False

    def onUpdate(self, _dt, _dt_optimal):
        if not self.running:
            return

        x, y = self.getPosition()
        if self.gw.isPressed("Left"):
            if self.moving != "L":
                self.setShape("./Recursos/Avion-L.png")
                self.moving = "L"
            x = x - self.speed
            self.setX(x)
        elif self.gw.isPressed("Right"):
            if self.moving != "R":
                self.setShape("./Recursos/Avion-R.png")
                self.moving = "R"
            x = x + self.speed
            self.setX(x)
        else:
            if self.moving != "C":
                self.setShape("./Recursos/Avion-C.png")
                self.moving = "C"
        if self.gw.isPressed("space") and time.time() - self.last_missil > 0.3:
            Misil(self.getX() + 6, self.getY() - 15, 3)
            self.last_missil = time.time()

        y = y - self.speed
        self.setY(y)

        if y < -20:
            self.stop()

    def onCollision(self, _dt, _dt_optimal, gobj):
        if not self.running:
            return

        if gobj.getTipo() in ["Explosion", "Esquirla"]:
            return

        x, y = self.getPosition()
        Explosion(x, y, self.getLayer(), "yellow")
        self.stop()
        self.setVisibility(False)
