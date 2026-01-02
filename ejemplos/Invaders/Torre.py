from MiniGameEngine.Sprite import Sprite


class Torre:
    def __init__(self, x, y, layer):
        TorrePart(x + 0, y, layer, "Recursos/Torre-000.png")
        TorrePart(x + 11, y, layer, "Recursos/Torre-001.png")
        TorrePart(x + 22, y, layer, "Recursos/Torre-001.png")
        TorrePart(x + 33, y, layer, "Recursos/Torre-002.png")
        TorrePart(x + 0, y + 8, layer, "Recursos/Torre-001.png")
        TorrePart(x + 11, y + 8, layer, "Recursos/Torre-001.png")
        TorrePart(x + 22, y + 8, layer, "Recursos/Torre-001.png")
        TorrePart(x + 33, y + 8, layer, "Recursos/Torre-001.png")
        TorrePart(x + 0, y + 16, layer, "Recursos/Torre-003.png")
        TorrePart(x + 11, y + 16, layer, "Recursos/Torre-004.png")
        TorrePart(x + 22, y + 16, layer, "Recursos/Torre-005.png")
        TorrePart(x + 33, y + 16, layer, "Recursos/Torre-006.png")


class TorrePart(Sprite):
    def __init__(self, x, y, layer, image_part):
        super().__init__(x, y, layer=layer, tipo="TorrePart", image_path=image_part)

        # receptor de colisiones
        self.setCollisionFlag(self.COLLISION_RECEIVER)

    def onCollision(self, _dt, _dt_optimal, _gobj):
        self.delete()
