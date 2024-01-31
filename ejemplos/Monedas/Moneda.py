from MiniGameEngine import GameObject


class Moneda(GameObject):
    # inicializamos el Alien
    def __init__(self, x, y):
        super().__init__(x, y, "Recursos/Moneda.png", "Moneda", collisions=True)

    # actualizamos fps veces por segundo
    def onUpdate(self, dt):
        pass

    # manejamos las colisiones
    def onCollision(self, dt, gobj):
        pass
