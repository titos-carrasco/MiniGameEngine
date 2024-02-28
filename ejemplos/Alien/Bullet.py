from MiniGameEngine.Sprite import Sprite


class Bullet(Sprite):
    # inicializamos la Bala
    def __init__(self, x, y):
        super().__init__(x, y, layer=1, tipo="Bullet", image_path="Recursos/Bullet.png")
        self.setCollisions(True)

    # actualizamos el estado de la Bala en cada frame
    def onUpdate(self, dt):
        y = self.getY()

        y = y - 300 * dt
        if y < 0:
            self.destroy()
        else:
            self.setY(y)

    # manejamos las colisiones
    def onCollision(self, dt, gobj):
        self.destroy()
