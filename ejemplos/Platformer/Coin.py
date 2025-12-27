from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Coin(Sprite):
    # inicializamos la Moneda
    def __init__(self, x, y):
        super().__init__(x, y, layer=1, tipo="Coin")

        # receptor de colisiones
        self.setCollisionFlag(self.COLLISION_RECEIVER)

        self.animator = Animator("Recursos/Tiles/coin*.png", self)

    # manejamos la actualizacion
    def onUpdate(self, dt, dt_optimal):
        self.animator.next()

    # manejamos las colisiones
    def onCollision(self, dt, dt_optimal, gobj):
        pass
