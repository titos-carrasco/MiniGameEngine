from MiniGameEngine.Sprite import Sprite


class Ball(Sprite):
    # inicializamos la pelota
    def __init__(self, x, y, speed_x, speed_y):
        super().__init__(x, y, layer=1, tipo="Ball", image_path="Recursos/Ball.png")

        # receptor de colisiones
        self.setCollisionFlag(self.COLLISION_INITIATOR)

        # variables internas
        self.speed_x = speed_x
        self.speed_y = speed_y

    # manejamos la actualizacion
    def onUpdate(self, dt, dt_optimal):
        x = self.getX() + dt * self.speed_x
        y = self.getY() + dt * self.speed_y

        # salí de la pantalla por la izquierda
        if x < 10:
            self.gw.out(-1)
            self.delete()
        # salí de la pantalla por la derecha
        elif x > self.gw.getWidth() - 10:
            self.gw.out(1)
            self.delete()

        # el juego continua
        else:
            # rebote en la parte superior
            if y < 10:
                y = 10
                self.speed_y = -self.speed_y
            # rebote en la parte inferior
            elif y > self.gw.getHeight() - 10:
                y = self.gw.getHeight() - 10
                self.speed_y = -self.speed_y

            # la nueva posición
            self.setPosition(x, y)

    # manejamos las colisiones
    def onCollision(self, dt, dt_optimal, gobj):
        if gobj.getTipo() == "Paleta":
            # me desplazaba hacia la derecha
            if self.speed_x > 0:
                x = gobj.getX() - self.getWidth()
            # me desplazaba hacia la izquierda
            else:
                x = gobj.getX() + gobj.getWidth()

            # ajusto la nueva posición
            self.setX(x)

            # invierto el sentido
            self.speed_x = -self.speed_x
