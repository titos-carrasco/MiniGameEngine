from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Pato(Sprite):
    def __init__(self, x, y):
        super().__init__(
            x, y, layer=1, tipo="Pato", image_path="Recursos/PatoVolando-000.png"
        )
        self.animator = Animator("Recursos/PatoVolando-*.png")
        self.animator.start()

    def onUpdate(self, dt):
        x = self.getX()
        w = self.getWidth()
        ww = self.getWorldWidth()

        imagePath = self.animator.next()
        if imagePath:
            self.setShape(imagePath)

        x = x + 5
        if x > ww:
            x = 0 - w
        self.setX(x)
