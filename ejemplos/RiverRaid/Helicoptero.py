from Explosion import Explosion
from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Helicoptero(Sprite):
    def __init__(self, x, y, layer, dir, gw):
        imagen = f"./Recursos/Helicoptero-{dir}1.png"
        super().__init__(x, y, layer=layer, tipo="Barco", image_path=imagen)
        self.setCollisionFlag(self.COLLISION_RECEIVER + self.COLLISION_INITIATOR)

        self.direccion = dir
        self.animLeft = Animator("./Recursos/Helicoptero-L*", self, 0.1)
        self.animRight = Animator("./Recursos/Helicoptero-R*", self, 0.1)
        if self.direccion == "R":
            self.animator = self.animRight
        else:
            self.animator = self.animLeft
        self.animator.start()

    def onUpdate(self, dt, _dt_optimal):
        _cx, cy = self.gw.getCamera().getPosition()
        _w, ch = self.gw.getCamera().getDimension()
        x, y = self.getPosition()
        _w, h = self.getDimension()

        if y + h < cy:
            return

        if  y > cy + ch:
            self.delete()
            return

        self.animator.next()

        if self.direccion == "R":
            x = x + 50 * dt
        else:
            x = x - 50 * dt
        self.setX(x)

    def onCollision(self, _dt, _dt_optimal, gobj):
        if gobj.getTipo() == "Tierra":
            if self.direccion == "R":
                self.animator = self.animLeft
                self.animator.start()
                self.direccion = "L"
            else:
                self.animator = self.animRight
                self.animator.start()
                self.direccion = "R"
        else:
            x, y = gobj.getPosition()
            Explosion(x, y, self.getLayer(), "red", npoints=80)
            self.delete()
