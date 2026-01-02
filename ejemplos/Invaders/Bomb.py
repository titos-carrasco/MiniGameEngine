from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Bomb(Sprite):
    def __init__(self, x, y, layer):
        super().__init__(x, y, layer=layer, tipo="Bomb")

        # iniciador de colisiones
        self.setCollisionFlag(self.COLLISION_INITIATOR)

        self.animator = Animator("Recursos/Bomb-*.png", self, speed=0.1)
        self.animator.start()

    # actualizamos el estado de la bomba en cada frame
    def onUpdate(self, _dt, dt_optimal):
        self.animator.next()

        y = self.getY()
        y = y + 100 * dt_optimal
        if y > 450:
            self.delete()
        else:
            self.setY(y)

    # manejamos las colisiones
    def onCollision(self, _dt, _dt_optimal, gobj):
        if gobj.getTipo() != "Invader":
            self.delete()
