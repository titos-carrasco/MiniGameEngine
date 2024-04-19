import random

from Explosion import Explosion
from MiniGameEngine.Sprite import Sprite


class Asteroid(Sprite):
    def __init__(self, rock=0, idx=0):
        super().__init__(0, 0, layer=1, tipo="Asteroide", debug=False)

        # la forma inicial
        if rock == 0:
            self.rock = random.randint(1, 3)
        else:
            self.rock = rock
        if idx == 0:
            self.idx = random.randint(1, 3)
        else:
            self.idx = idx

        self.setShape(f"Recursos/Roca_{self.rock}_{self.idx}.png")

        # la velocidad
        self.speed_x = random.choice([-2, -1, 1, 2]) * 50
        self.speed_y = random.choice([-2, -1, 1, 2]) * 50

        # la posicion inicial
        x = random.randint(-self.getWidth(), self.gw.getWidth())
        if self.speed_y > 0:
            y = -self.getHeight()
        else:
            y = self.gw.getHeight()
        self.setPosition(x, y)

        # ajustamos colisionador
        w, h = self.getDimension()
        factor = 0.15
        self.setCollider(w * factor, h * factor, w * factor, h * factor)

        # receptor de colisiones
        self.setCollisionFlag(self.COLLISION_RECEIVER)

    # manejamos la actualizacion
    def onUpdate(self, dt, dt_optimal):
        x, y = self.getPosition()
        x = x + self.speed_x * dt
        y = y + self.speed_y * dt
        self.setPosition(x, y)

        # sali de pantalla, aviso que me voy a destruir
        if (
            y <= -self.getHeight()
            or y > self.gw.getHeight()
            or x <= -self.getWidth()
            or x > self.gw.getWidth()
        ):
            self.gw.message("Asteroide Out", self)
            self.delete()

    # manejamos las colisiones
    def onCollision(self, dt, dt_optimal, gobj):
        tipo = gobj.getTipo()
        if tipo != "Bullet":
            return

        self.gw.message("Asteroide Hit", self)
        rock = self.rock
        speed_x = self.speed_x
        speed_y = self.speed_y
        x, y = self.getPosition()
        w, h = self.getDimension()
        self.delete()
        Explosion(x + w / 2, y + h / 2)
