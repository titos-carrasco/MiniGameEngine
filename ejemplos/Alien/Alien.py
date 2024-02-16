from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator

from Explosion import Explosion


class Alien(Sprite):
    # inicializamos el Alien
    def __init__(self, x, y):
        super().__init__(
            x, y, layer=1, tipo="Alien", image_path="Recursos/Alien-002.png"
        )
        self.setCollisions(True)

        self.animator = Animator("Recursos/Alien-*.png", speed=0.6)
        self.animator.start()

    # manejamos la actualizacion
    def onUpdate(self, dt):
        imagePath = self.animator.next()
        if imagePath:
            self.setShape(imagePath)

    # manejamos las colisiones
    def onCollision(self, dt, gobj):
        if gobj.getTipo() == "Bullet":
            x, y = self.getPosition()
            self.destroy()
            Explosion(x - 2, y - 6)
            print("Alien:me dieron")
