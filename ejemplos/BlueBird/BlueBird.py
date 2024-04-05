import random

from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class BlueBird(Sprite):
    # inicializamos el Ave
    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            layer=1,
            tipo="BlueBird",
            debug=True,
        )

        # iniciador y receptos de colisiones
        self.setCollisionFlag(self.COLLISION_INITIATOR + self.COLLISION_RECEIVER)

        self.speed = random.randint(100, 160)
        self.animator = Animator("Recursos/bird-*.png")
        image_path = self.animator.start()
        self.setShape(image_path)

    # actualizamos 1/fps veces por segundo
    def onUpdate(self, dt, dt_optimal):
        x = self.getX()
        w = self.getWidth()
        ww = self.gw.getWidth()

        image_path = self.animator.next()
        if image_path:
            self.setShape(image_path)

        x = x + self.speed * dt_optimal
        if x > ww:
            x = 0 - w
        self.setX(x)
