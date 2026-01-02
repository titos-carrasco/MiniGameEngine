from MiniGameEngine.Sprite import Sprite


class Missil(Sprite):
    def __init__(self, x, y, layer):
        super().__init__(
            x, y, layer=layer, tipo="Missil", image_path="Recursos/Missil.png"
        )

        # iniciador de colisiones
        self.setCollisionFlag(self.COLLISION_INITIATOR)

    # actualizamos el estado del misil en cada frame
    def onUpdate(self, _dt, dt_optimal):
        y = self.getY()

        y = y - 300 * dt_optimal
        if y < 0:
            self.delete()
        else:
            self.setY(y)

    # manejamos las colisiones
    def onCollision(self, _dt, _dt_optimal, _gobj):
        self.delete()
