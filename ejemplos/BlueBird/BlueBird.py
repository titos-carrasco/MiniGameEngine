import time
import random

from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.ImageAnimator import ImageAnimator


class BlueBird(Sprite):
    # inicializamos el Ave
    def __init__(self, x, y):
        super().__init__(
            x, y, layer=1, tipo="BlueBird", imagePath="Recursos/bird-000.png"
        )
        self.speed = random.randint(1, 6)
        self.animator = ImageAnimator("Recursos/bird-*.png")
        self.animator.start()

    # actualizamos 1/fps veces por segundo
    def onUpdate(self, dt):
        x = self.getX()
        w = self.getWidth()
        ww = self.getWorldWidth()

        imagePath = self.animator.next()
        if imagePath:
            self.setShape(imagePath)

        x = x + self.speed
        if x > ww:
            x = 0 - w
        self.setX(x)
