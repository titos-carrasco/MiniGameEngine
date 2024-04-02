from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Bomb(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, layer=1, tipo="Bomb")

        self.setCollisions(True)
        self.animator = Animator("Recursos/Bomb-*.png", speed=0.1)
        image_path = self.animator.start()
        self.setShape(image_path)

    # actualizamos el estado de la bomba en cada frame
    def onUpdate(self, dt, dt_optimal):
        image_path = self.animator.next()
        if image_path:
            self.setShape(image_path)

        y = self.getY()
        y = y + 100 * dt_optimal
        if y > 450:
            self.delete()
        else:
            self.setY(y)

    # manejamos las colisiones
    def onCollision(self, dt, dt_optimal, gobj):
        if gobj.getTipo() != "Invader":
            self.delete()
