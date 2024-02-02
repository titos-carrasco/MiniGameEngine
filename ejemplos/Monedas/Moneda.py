from MiniGameEngine import GameObject


class Moneda(GameObject):
    # inicializamos la Moneda
    def __init__(self, x, y, layer=1):
        super().__init__(
            x,
            y,
            imagePath="Recursos/Moneda.png",
            tipo="Moneda",
            collisions=True,
            layer=layer,
        )

    # actualizamos 1/fps veces por segundo
    def onUpdate(self, dt):
        pass

    # manejamos las colisiones
    def onCollision(self, dt, gobj):
        pass
