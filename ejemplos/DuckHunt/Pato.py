from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Pato(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, layer=1, tipo="Pato")
        self.animator = Animator("Recursos/PatoVolando-*.png", self)

    def onUpdate(self, dt, dt_optimal):
        x = self.getX()
        w = self.getWidth()
        ww = self.gw.getWidth()

        self.animator.next()

        x = x + 100 * dt_optimal
        if x > ww:
            x = 0 - w
        self.setX(x)
