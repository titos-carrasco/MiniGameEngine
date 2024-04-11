from MiniGameEngine.Sprite import Sprite


class Paleta(Sprite):
    # inicializamos la paleta del computador
    def __init__(self, x, y):
        super().__init__(x, y, layer=1, tipo="Paleta", image_path="Recursos/Paleta.png")

        # receptor de colisiones
        self.setCollisionFlag(self.COLLISION_RECEIVER)

        # para saber si debo actuar
        self.playing = False

    # manejamos la actualizacion
    def onUpdate(self, dt, dt_optimal):
        if self.playing:
            x, y = self.getPosition()
            bx, by = self.gw.getBallPosition()

            if y < by:
                y = y + dt * 200
                lim = self.gw.getHeight() - self.getHeight() - 10
                if y > lim:
                    y = lim
                self.setY(y)
            elif y > by:
                y = y - dt * 200
                if y < 10:
                    y = 10
                self.setY(y)

    def play(self):
        self.playing = True

    def stop(self):
        self.playing = False
