from MiniGameEngine.Sprite import Sprite


class Base(Sprite):
    # inicializamos la base
    def __init__(self, x, y, layer, distance_x=0, vx=0, distance_y=0, vy=0):
        super().__init__(
            x,
            y,
            layer=layer,
            tipo="Base",
            image_path="Recursos/Base.png",
            debug=True,
        )
        self.distance_x = distance_x
        self.distance_y = distance_y
        self.vx = -vx
        self.vy = -vy

        self.setCollider(6, 0, 6, 54)
        self.setCollisions(True)

        self.origin_x = x
        self.origin_y = y
        self.dx = 0
        self.dy = 0

    def getDisplacement(self):
        return self.dx, self.dy

    # manejamos la actualizacion
    def onUpdate(self, dt, dt_optimal):
        x_ = self.getX()
        x = x_ + int(self.vx * dt_optimal)
        self.dx = x_ - x

        if x < self.origin_x - self.distance_x or x > self.origin_x + self.distance_x:
            self.vx = self.vx * -1

        y_ = self.getY()
        y = y_ + int(self.vy * dt_optimal)
        self.dy = y_ - y

        if y < self.origin_y - self.distance_y or y > self.origin_y + self.distance_y:
            self.vy = self.vy * -1

        self.setPosition(x, y)
