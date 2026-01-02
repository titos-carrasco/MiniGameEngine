from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Coin(Sprite):
    # inicializamos la Moneda
    def __init__(self, x, y, layer):
        super().__init__(x, y, layer=layer, tipo="Coin")

        # receptor de colisiones
        self.setCollisionFlag(self.COLLISION_RECEIVER)

        self.animator = Animator("Recursos/Tiles/coin*.png", self)
        self.animator.start()

    # manejamos la actualizacion
    def onUpdate(self, _dt, _dt_optimal):
        self.animator.next()

    # manejamos las colisiones
    def onCollision(self, _dt, _dt_optimal, _gobj):
        pass
