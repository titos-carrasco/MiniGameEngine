from Explosion import Explosion
from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Alien(Sprite):
    # inicializamos el Alien
    def __init__(self, x, y):
        super().__init__(x, y, layer=1, tipo="Alien")
        self.setCollisions(True)

        self.animator = Animator("Recursos/Alien-*.png", speed=0.6)
        image_path = self.animator.start()
        self.setShape(image_path)

    # manejamos la actualizacion
    def onUpdate(self, dt, dt_optimal):
        image_path = self.animator.next()
        if image_path:
            self.setShape(image_path)

    # manejamos las colisiones
    def onCollision(self, dt, dt_optimal, gobj):
        if gobj.getTipo() == "Bullet":
            x, y = self.getPosition()
            self.delete()
            Explosion(x - 2, y - 6)
            print("Alien:me dieron")
