import time

from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Animation(Sprite):
    def __init__(self, x, y, images_path, speed=0.6, duration=0):
        super().__init__(x, y, layer=1, tipo="Animacion")

        self.animator = Animator(images_path, speed=speed)
        image_path = self.animator.start()
        self.setShape(image_path)

        self.duration = duration
        self.t = time.time()

    def onUpdate(self, dt, dt_optimal):
        image_path = self.animator.next()
        if image_path:
            self.setShape(image_path)

        if self.duration > 0:
            if time.time() - self.t > self.duration:
                self.delete()
