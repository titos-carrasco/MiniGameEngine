from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Box import Box

class Base(Sprite):
    # inicializamos la base
    def __init__(self, x, y):
        super().__init__(x, y, layer=1, tipo="Base", image_path="Recursos/Base.png")

        self.suelo = Box(x+8, y, 112, 8, 1, "Suelo", border=0, debug=True)
        self.suelo.setCollisions(True)

        self.dy = -90

    # manejamos la actualizacion
    def onUpdate(self, dt, dt_optimal):
        y = self.getY() + self.dy * dt_optimal

        if y < 200 or y > 300:
            self.dy = self.dy * -1

        self.setY(y)
        self.suelo.setY(y)
