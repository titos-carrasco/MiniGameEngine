import time
from MiniGameEngine import GameObject
from MiniGameEngine import ObjectAnimator


class BlueBird(GameObject):
    # inicializamos el Ave
    def __init__(self, x, y):
        super().__init__(x, y, imagePath=None, tipo="BlueBird")
        self.animator = ObjectAnimator(self, imagesPath="Recursos/bird-*.png")
        self.animator.start()

    # actualizamos 1/fps veces por segundo
    def onUpdate(self, dt):
        self.animator.animate()
