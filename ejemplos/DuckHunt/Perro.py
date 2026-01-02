from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Perro(Sprite):
    def __init__(self, x, y, layer):
        super().__init__(x, y, layer=layer, tipo="Perro")
        self.animator = Animator("Recursos/PerroCaminando-*.png", self)
        self.animator.start()

    def onUpdate(self, _dt, dt_optimal):
        x = self.getX()
        w = self.getWidth()
        ww = self.gw.getWidth()

        self.animator.next()

        x = x + 120 * dt_optimal
        if x > ww:
            x = 0 - w
        self.setX(x)
