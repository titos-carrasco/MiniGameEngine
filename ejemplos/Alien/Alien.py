from MiniGameEngine import GameObject


class Alien(GameObject):
    # inicializamos el Alien
    def __init__(self, x, y):
        super().__init__(
            x, y, imagePath="Recursos/Alien.png", tipo="Alien", collisions=True
        )

    # manejamos las colisiones
    def onCollision(self, dt, gobj):
        if gobj.getTipo() == "Bullet":
            self.destroy()
            print("Alien:me dieron")
