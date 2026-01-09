import random
from MiniGameEngine.Box import Box
from MiniGameEngine.EmptyObject import EmptyObject


class Explosion(EmptyObject):
    def __init__(self, x, y, layer, color, npoints=50):
        super().__init__(x, y, 1, 1, layer=layer, tipo="Explosion")

        x1 = int(x)
        y1 = int(y)
        r = 20
        for _e in range(10):
            x2 = random.randint(x1 - r, x1 + r)
            y2 = random.randint(y1 - r, y1 + r)
            Esquirla(x, y, x2, y2, layer, color, npoints)

    # solo vivimos 1 frame
    def onUpdate(self, _dt, _dt_optimal):
        self.delete()


class Esquirla(Box):
    def __init__(self, x1, y1, x2, y2, layer, color, npoints):
        super().__init__(
            x1, y1, 3, 3, layer, tipo="Esquirla", border_color=color, fill_color=color
        )
        cantidad_p = random.randint(npoints - 10, npoints + 10)
        distancia_x = x2 - x1
        distancia_y = y2 - y1
        delta_x = distancia_x / cantidad_p
        delta_y = distancia_y / cantidad_p

        self.puntos = []
        for i in range(cantidad_p):
            self.puntos.append((x1 + delta_x * i, y1 + delta_y * i))

    def onUpdate(self, _dt, _dt_optimal):
        try:
            x, y = self.puntos.pop(0)
            self.setPosition(x, y)
        except IndexError as _e:
            self.delete()
