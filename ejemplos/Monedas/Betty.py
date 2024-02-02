from MiniGameEngine import GameObject
from MiniGameEngine import ObjectAnimator


class Betty(GameObject):
    # inicializamos a Betty
    def __init__(self, x, y, layer=1):
        super().__init__(
            x, y, imagePath=None, tipo="Betty", collisions=True, layer=layer
        )
        self.images = {
            "Right": "Recursos/BettyRight.png",
            "Left": "Recursos/BettyLeft.png",
        }
        for i in self.images:
            self.loadImage(self.images[i])
        self.direccion = "Right"
        self.setShape(self.images[self.direccion])

    # actualizamos 1/fps veces por segundo
    def onUpdate(self, dt):
        ww = self.getWorldWidth()
        w = self.getWidth()
        x = self.getX()
        y = self.getY()

        # movimiento lateral
        if self.isPressed("Left"):
            x = x - 4
            if x - w / 2 < 0:
                x = w / 2
            if self.direccion != "Left":
                self.direccion = "Left"
                self.setShape(self.images["Left"])
        elif self.isPressed("Right"):
            x = x + 4
            if x > ww - w / 2:
                x = ww - w / 2
            if self.direccion != "Right":
                self.direccion = "Right"
                self.setShape(self.images["Right"])
        self.setPosition(x, y)

    # manejamos las colisiones
    def onCollision(self, dt, gobj):
        print("Betty: Colisione con", gobj.getTipo())
