import time
import random

from MiniGameEngine.Sprite import Sprite


class Explosion(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, layer=1, tipo="Explosion")

        x1 = int(x)
        y1 = int(y)
        r = 50
        for e in range(20):
            x2 = random.randint(x1 - r, x1 + r)
            y2 = random.randint(y1 - r, y1 + r)
            Esquirla(x, y, x2, y2)

    # solo vivimos 1 frame
    def onUpdate(self, dt, dt_optimal):
        self.delete()


class Esquirla(Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(
            x1, y1, layer=1, tipo="Esquirla", image_path="Recursos/Bullet.png"
        )
        cantidad_p = random.randint(20, 100)
        distancia_x = x2 - x1
        distancia_y = y2 - y1
        delta_x = distancia_x / cantidad_p
        delta_y = distancia_y / cantidad_p

        self.puntos = []
        for i in range(cantidad_p):
            self.puntos.append((x1 + delta_x * i, y1 + delta_y * i))

    def onUpdate(self, dt, dt_optimal):
        try:
            x, y = self.puntos.pop(0)
            self.setPosition(x, y)
        except:
            self.delete()
