from Explosion import Explosion
from MiniGameEngine.Sprite import Sprite


class Barco(Sprite):
    def __init__(self, x, y, layer, direccion, gw):
        imagen = f"./Recursos/Barco-{direccion}.png"
        super().__init__(x, y, layer=layer, tipo="Barco", image_path=imagen)
        self.gw = gw

        self.setCollisionFlag(self.COLLISION_RECEIVER + self.COLLISION_INITIATOR)
        self.direccion = direccion

    def onUpdate(self, dt, _dt_optimal):
        _cx, cy = self.gw.getCamera().getPosition()
        _w, ch = self.gw.getCamera().getDimension()
        x, y = self.getPosition()
        _w, h = self.getDimension()

        if y + h < cy:
            return

        if y > cy + ch:
            self.delete()
            return

        if self.direccion == "R":
            x = x + 50 * dt
        else:
            x = x - 50 * dt
        self.setX(x)

    def onCollision(self, _dt, _dt_optimal, gobj):
        if gobj.getTipo() == "Tierra":
            if self.direccion == "R":
                self.setShape("./Recursos/Barco-L.png")
                self.direccion = "L"
            else:
                self.setShape("./Recursos/Barco-R.png")
                self.direccion = "R"
        else:
            self.gw.addPoints(20)
            x, y = gobj.getPosition()
            Explosion(x, y, self.getLayer(), "red", npoints=80)
            self.delete()
