from MiniGameEngine.Sprite import Sprite


class Bullet(Sprite):
    # inicializamos la Bala
    def __init__(self, x, y):
        super().__init__(x, y, layer=2, tipo="Bullet", image_path="Recursos/Bullet.png")

        # iniciador de colisiones
        self.setCollisionFlag(self.COLLISION_INITIATOR)

    # actualizamos el estado de la Bala en cada frame
    def onUpdate(self, dt, dt_optimal):
        y = self.getY()
        y = y - 300 * dt_optimal
        if y < 0:
            self.delete()
        else:
            self.setY(y)

    # manejamos las colisiones
    def onCollision(self, dt, dt_optimal, gobj):
        self.delete()
