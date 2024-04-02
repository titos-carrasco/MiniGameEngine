from MiniGameEngine.Sprite import Sprite


class Missil(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, layer=1, tipo="Missil", image_path="Recursos/Missil.png")
        self.setCollisions(True)

    # actualizamos el estado del misil en cada frame
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
