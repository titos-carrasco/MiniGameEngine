import time
from MiniGameEngine import GameObject
from MiniGameEngine import ObjectAnimator


class BlueBird(GameObject):
    # inicializamos el Ave
    def __init__(self, x, y):
        super().__init__(x, y, "Recursos/bird-*.png", "BlueBird")
        self.animator = ObjectAnimator(self)
        self.animator.start()

    # actualizamos fps veces por segundo
    def onUpdate(self, dt):
        self.animator.animate()
