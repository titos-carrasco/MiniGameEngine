from MiniGameEngine.Sprite import Sprite


class Escalera(Sprite):
    # inicializamos la Escalera
    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            layer=1,
            tipo="Escalera",
            image_path="Recursos/Escalera.png",
            debug=True,
        )

        # receptor de colisiones
        self.setCollider(30, 10, 30, 0)
        self.setCollisionFlag(self.COLLISION_RECEIVER)
