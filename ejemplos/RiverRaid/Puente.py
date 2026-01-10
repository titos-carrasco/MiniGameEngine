from Explosion import Explosion
from MiniGameEngine.Sprite import Sprite


class Puente(Sprite):
    def __init__(self, x, y, layer, gw):
        super().__init__(
            x, y, layer=layer, tipo="Puente", image_path="./Recursos/Puente.png"
        )
        self.setCollisionFlag(self.COLLISION_RECEIVER)
        self.gw = gw

    def onCollision(self, _dt, _dt_optimal, gobj):
        self.gw.addPoints(10)
        x, y = gobj.getPosition()
        Explosion(x, y, self.getLayer(), "brown", npoints=100)
        self.delete()
