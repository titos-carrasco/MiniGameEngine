from MiniGameEngine.Sprite import Sprite


class Bullet(Sprite):
    # inicializamos la Bala
    def __init__(self, x, y, dx, dy):
        super().__init__(
            x, y, layer=1, tipo="Bullet", image_path="Recursos/Bullet.png", debug=False
        )

        # ajustamos colisionador
        self.setCollider(13, 13, 13, 13)

        # iniciador de colisiones
        self.setCollisionFlag(self.COLLISION_INITIATOR)

        # para el ángulo de disparo
        self.dx = dx
        self.dy = dy

    # actualizamos el estado de la Bala en cada frame
    def onUpdate(self, dt, dt_optimal):
        x, y = self.getPosition()

        x = x + dt * self.dx * 200
        y = y + dt * self.dy * 200

        if x < 0 or x > self.gw.getWidth() or y < 0 or y > self.gw.getHeight():
            self.delete()
        else:
            self.setPosition(x, y)

    # manejamos las colisiones
    def onCollision(self, dt, dt_optimal, gobj):
        tipo = gobj.getTipo()
        if tipo == "Asteroide":
            self.delete()
