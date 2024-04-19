import time

from Bullet import Bullet

from MiniGameEngine.Sprite import Sprite


class SpaceShip(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, layer=1, tipo="SpaceShip", debug=False)

        # receptor de colisiones
        self.setCollisionFlag(self.COLLISION_RECEIVER + self.COLLISION_INITIATOR)

        # formas
        self.shapes = [
            ["Nave_0.png", 1, 0],
            ["Nave_45.png", 1, -1],
            ["Nave_90.png", 0, -1],
            ["Nave_135.png", -1, -1],
            ["Nave_180.png", -1, 0],
            ["Nave_225.png", -1, 1],
            ["Nave_270.png", 0, 1],
            ["Nave_315.png", 1, 1],
        ]
        self.shape = 0
        self.setShape("Recursos/" + self.shapes[self.shape][0])

        # ajustamos colisionador
        self.setCollider(10, 10, 10, 10)

        # velocidad actual
        self.speed_x = 0
        self.speed_y = 0
        self.v = 0

        # control del tiempo entre teclas
        self.last_k = 0
        self.last_b = 0

    # actualizamos el estado de la Nave Espacial en cada frame
    def onUpdate(self, dt, dt_optimal):
        x, y = self.getPosition()

        # verificamos las teclas cada cierto tiempo
        t = time.time()
        if t - self.last_k > 0.100:
            self.last_k = t

            # giro a la derecha
            if self.gw.isPressed("Right"):
                self.shape = self.shape - 1
                if self.shape < 0:
                    self.shape = len(self.shapes) - 1
                shape, vx, vy = self.shapes[self.shape]
                self.setShape("Recursos/" + shape)
                self.v = 0

            # giro a la izquierda
            elif self.gw.isPressed("Left"):
                self.shape = self.shape + 1
                if self.shape >= len(self.shapes):
                    self.shape = 0
                shape, vx, vy = self.shapes[self.shape]
                self.setShape("Recursos/" + shape)
                self.v = 0

            # avanzar
            elif self.gw.isPressed("Up"):
                self.v = min(self.v + 20, 150)
                shape, vx, vy = self.shapes[self.shape]
                self.speed_x = vx * self.v
                self.speed_y = vy * self.v

            # frenar
            elif self.gw.isPressed("Down"):
                self.v = max(0, self.v - 20)
                shape, vx, vy = self.shapes[self.shape]
                self.speed_x = vx * self.v
                self.speed_y = vy * self.v

            # disparar
            if self.gw.isPressed("space"):
                if t - self.last_b > 0.5:
                    shape, vx, vy = self.shapes[self.shape]
                    bullet = Bullet(x, y, vx, vy)
                    bx, by = bullet.getDimension()
                    bx = x - bx / 2 + self.getWidth() / 2 + self.getWidth() / 2 * vx
                    by = y - by / 2 + self.getHeight() / 2 + self.getHeight() / 2 * vy
                    bullet.setPosition(bx, by)
                    self.last_b = t

        # la nueva posición
        x = x + dt * self.speed_x
        y = y + dt * self.speed_y
        self.setPosition(x, y)

    # manejamos las colisiones
    def onCollision(self, dt, dt_optimal, gobj):
        tipo = gobj.getTipo()
        if tipo != "Asteroide":
            return

        print("Choque con un asteroide")
