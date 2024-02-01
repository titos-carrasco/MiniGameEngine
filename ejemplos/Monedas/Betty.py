from MiniGameEngine import GameObject


class Betty(GameObject):
    # inicializamos el Alien
    def __init__(self, x, y, layer=1):
        super().__init__(
            x, y, "Recursos/Betty-R.png", "Betty", collisions=True, layer=layer
        )
        self.direccion = "R"

    # actualizamos /1fps veces
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
            if self.direccion != "L":
                self.direccion = "L"
                self.setShape("Recursos/Betty-L.png")
        elif self.isPressed("Right"):
            x = x + 4
            if x > ww - w / 2:
                x = ww - w / 2
            if self.direccion != "R":
                self.direccion = "R"
                self.setShape("Recursos/Betty-R.png")
        self.setPosition(x, y)

    # manejamos las colisiones
    def onCollision(self, dt, gobj):
        print("Betty: Colisione con", gobj.getTipo())
