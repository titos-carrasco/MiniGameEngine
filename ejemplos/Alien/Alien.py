from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator
from MiniGameEngine.Animation import Animation


class Alien(Sprite):
    # inicializamos el Alien
    def __init__(self, x, y, layer):
        super().__init__(x, y, layer=layer, tipo="Alien")

        # receptor de colisiones
        self.setCollisionFlag(self.COLLISION_RECEIVER)

        self.animator = Animator("Recursos/Alien-*.png", self, speed=0.6)
        self.animator.start()

    # manejamos la actualizacion
    def onUpdate(self, _dt, _dt_optimal):
        self.animator.next()

    # manejamos las colisiones
    def onCollision(self, _dt, _dt_optimal, gobj):
        if gobj.getTipo() == "Bullet":
            x, y = self.getPosition()
            Animation(x - 2, y - 6, "Recursos/Explosion-*.png", speed=0.1)
            print("Alien:me dieron")
            self.delete()
