from MiniGameEngine.Sprite import Sprite


class Human(Sprite):
    # inicializamos la paleta del humano
    def __init__(self, x, y):
        super().__init__(x, y, layer=1, tipo="Paleta", image_path="Recursos/Paleta.png")

        # receptor de colisiones
        self.setCollisionFlag(self.COLLISION_RECEIVER)

        # variables internas
        self.speed = 200

    # manejamos la actualizacion
    def onUpdate(self, dt, dt_optimal):
        if self.gw.isPressed("Up"):
            lim = 10
            y = self.getY() - dt * self.speed
            if y < lim:
                y = lim
            self.setY(y)
        elif self.gw.isPressed("Down"):
            lim = self.gw.getHeight() - self.getHeight() - 10
            y = self.getY() + dt * self.speed
            if y > lim:
                y = lim
            self.setY(y)
