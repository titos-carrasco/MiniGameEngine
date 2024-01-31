import time
from MiniGameEngine import GameObject


class BlueBird(GameObject):
    # inicializamos el Ave
    def __init__(self, x, y):
        super().__init__(x, y, "Recursos/bird-000.png", "BlueBird")

        self.images = [
            "Recursos/bird-000.png",
            "Recursos/bird-001.png",
            "Recursos/bird-002.png",
            "Recursos/bird-003.png",
            "Recursos/bird-004.png",
            "Recursos/bird-005.png",
            "Recursos/bird-006.png"
        ]
        self.loadImages(self.images)
        self.actual = 0
        self.t = time.time()

    # actualizamos fps veces por segundo
    def onUpdate(self, dt):
        if(time.time() - self.t > 0.05):
            self.actual = self.actual + 1
            if(self.actual >= len(self.images)):
                self.actual = 0
            self.setShape(self.images[self.actual])
            self.t = time.time()


    # manejamos las colisiones
    def onCollision(self, dt, gobj):
        pass
