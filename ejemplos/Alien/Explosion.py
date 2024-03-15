from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Explosion(Sprite):
    def __init__(self, x, y):
        super().__init__(
            x, y, layer=2, tipo="Explosion", image_path="Recursos/Explosion-001.png"
        )
        self.animator = Animator("Recursos/Explosion-*.png", speed=0.1, repeat=False)
        self.setShape(self.animator.start())

    # actualizamos 1/fps veces por segundo
    def onUpdate(self, dt, dt_optimal):
        if not self.animator.isRunning():
            self.animator = None
            self.delete()
            return

        image_path = self.animator.next()
        if image_path:
            self.setShape(image_path)
