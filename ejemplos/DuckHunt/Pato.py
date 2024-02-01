import time
from MiniGameEngine import GameObject


class Pato(GameObject):
    def __init__(self, x, y, layer=1):
        super().__init__(x, y, "Recursos/PatoVolando-000.png", "Perro", layer=layer)
        self.estado = "volando"
        self.t = 0
        self.idx = 0

        self.PatoVolando = [
            "Recursos/PatoVolando-000.png",
            "Recursos/PatoVolando-001.png",
            "Recursos/PatoVolando-002.png",
        ]
        self.loadImages(self.PatoVolando)

    def onUpdate(self, dt):
        x = self.getX()
        y = self.getY()
        w = self.getWidth()
        ww = self.getWorldWidth()

        if self.estado == "volando":
            if time.time() - self.t > 0.100:
                self.idx = self.idx + 1
                if self.idx >= len(self.PatoVolando):
                    self.idx = 0
                self.setShape(self.PatoVolando[self.idx])
                self.t = time.time()
                x = x + 16
                if x - w / 2 > ww:
                    x = 0 - w / 2
                self.setPosition(x, y)
