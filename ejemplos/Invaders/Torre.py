from MiniGameEngine.Sprite import Sprite


class Torre:
    def __init__(self, x, y):
        TorrePart(x + 0, y, "Recursos/Torre-000.png")
        TorrePart(x + 11, y, "Recursos/Torre-001.png")
        TorrePart(x + 22, y, "Recursos/Torre-001.png")
        TorrePart(x + 33, y, "Recursos/Torre-002.png")
        TorrePart(x + 0, y + 8, "Recursos/Torre-001.png")
        TorrePart(x + 11, y + 8, "Recursos/Torre-001.png")
        TorrePart(x + 22, y + 8, "Recursos/Torre-001.png")
        TorrePart(x + 33, y + 8, "Recursos/Torre-001.png")
        TorrePart(x + 0, y + 16, "Recursos/Torre-003.png")
        TorrePart(x + 11, y + 16, "Recursos/Torre-004.png")
        TorrePart(x + 22, y + 16, "Recursos/Torre-005.png")
        TorrePart(x + 33, y + 16, "Recursos/Torre-006.png")


class TorrePart(Sprite):
    def __init__(self, x, y, image_part):
        super().__init__(x, y, layer=1, tipo="TorrePart", image_path=image_part)

        # receptor de colisiones
        self.setCollisionFlag(self.COLLISION_RECEIVER)

    def onCollision(self, dt, dt_optimal, gobj):
        self.delete()
