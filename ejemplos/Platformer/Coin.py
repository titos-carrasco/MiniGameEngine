from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Coin(Sprite):
    # inicializamos la Moneda
    def __init__(self, x, y):
        super().__init__(x, y, layer=1, tipo="Coin")
        self.setCollisions(True)

        self.animator = Animator("Recursos/Tiles/coin*.png", speed=0.1)
        image_path = self.animator.start()
        self.setShape(image_path)

    # manejamos la actualizacion
    def onUpdate(self, dt, dt_optimal):
        image_path = self.animator.next()
        if image_path:
            self.setShape(image_path)

    # manejamos las colisiones
    def onCollision(self, dt, dt_optimal, gobj):
        pass
