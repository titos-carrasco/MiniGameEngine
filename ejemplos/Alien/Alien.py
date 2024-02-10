from MiniGameEngine.Sprite import Sprite


class Alien(Sprite):
    # inicializamos el Alien
    def __init__(self, x, y):
        super().__init__(x, y, layer=1, tipo="Alien", imagePath="Recursos/Alien.png")
        self.setCollisions(True)

    # manejamos las colisiones
    def onCollision(self, dt, gobj):
        if gobj.getTipo() == "Bullet":
            self.destroy()
            print("Alien:me dieron")
