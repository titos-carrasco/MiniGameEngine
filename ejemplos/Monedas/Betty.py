from MiniGameEngine.Sprite import Sprite


class Betty(Sprite):
    # inicializamos a Betty
    def __init__(self, x, y, layer):
        super().__init__(
            x, y, tipo="Betty", layer=layer, image_path="Recursos/BettyRight.png"
        )

        # iniciador de colisiones
        self.setCollisionFlag(self.COLLISION_INITIATOR)

        self.images = {
            "Right": "Recursos/BettyRight.png",
            "Left": "Recursos/BettyLeft.png",
        }
        self.direccion = "Right"

    # actualizamos 1/fps veces por segundo
    def onUpdate(self, dt, dt_optimal):
        ww = self.gw.getWidth()
        w = self.getWidth()
        x = self.getX()

        # movimiento lateral
        if self.gw.isPressed("Left"):
            x = x - 200 * dt_optimal
            x = max(x, 0)
            self.setX(x)
            if self.direccion != "Left":
                self.direccion = "Left"
                self.setShape(self.images["Left"])
        elif self.gw.isPressed("Right"):
            x = x + 200 * dt_optimal
            if x + w > ww:
                x = ww - w
            self.setX(x)
            if self.direccion != "Right":
                self.direccion = "Right"
                self.setShape(self.images["Right"])

    # manejamos las colisiones
    def onCollision(self, dt, dt_optimal, gobj):
        print("Betty: Colisione con", gobj.getTipo())
