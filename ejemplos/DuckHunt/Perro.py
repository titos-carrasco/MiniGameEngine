from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Perro(Sprite):
    def __init__(self, x, y):
        super().__init__(
            x, y, layer=3, tipo="Perro", image_path="Recursos/PerroCaminando-000.png"
        )
        self.animator = Animator("Recursos/PerroCaminando-*.png")
        self.animator.start()

    def onUpdate(self, dt):
        x = self.getX()
        w = self.getWidth()
        ww = self.getWorldWidth()

        imagePath = self.animator.next()
        if imagePath:
            self.setShape(imagePath)

        x = x + 2
        if x > ww:
            x = 0 - w
        self.setX(x)
