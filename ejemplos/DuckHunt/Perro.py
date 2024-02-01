import time
from MiniGameEngine import GameObject


class Perro(GameObject):
    def __init__(self, x, y, layer=3):
        super().__init__(x, y, "Recursos/PerroCaminando-000.png", "Perro", layer=layer)
        self.estado = "caminando"
        self.t = 0
        self.idx = 0

        self.PerroCaminando = [
            "Recursos/PerroCaminando-000.png",
            "Recursos/PerroCaminando-001.png",
            "Recursos/PerroCaminando-002.png",
            "Recursos/PerroCaminando-003.png",
        ]
        self.loadImages(self.PerroCaminando)

    def onUpdate(self, dt):
        x = self.getX()
        y = self.getY()
        w = self.getWidth()
        ww = self.getWorldWidth()

        if self.estado == "caminando":
            if time.time() - self.t > 0.100:
                self.idx = self.idx + 1
                if self.idx >= len(self.PerroCaminando):
                    self.idx = 0
                self.setShape(self.PerroCaminando[self.idx])
                self.t = time.time()
                x = x + 8
                if x - w / 2 > ww:
                    x = 0 - w / 2
                self.setPosition(x, y)
