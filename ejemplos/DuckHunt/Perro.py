from MiniGameEngine import GameObject
from MiniGameEngine import ObjectAnimator


class Perro(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, imagePath=None, tipo="Perro", layer=3)
        self.animator = ObjectAnimator(self, imagesPath="Recursos/PerroCaminando-*")
        self.animator.start()

    def onUpdate(self, dt):
        x = self.getX()
        y = self.getY()
        w = self.getWidth()
        ww = self.getWorldWidth()

        if self.animator.animate():
            x = x + 8
            if x - w / 2 > ww:
                x = 0 - w / 2
            self.setPosition(x, y)
