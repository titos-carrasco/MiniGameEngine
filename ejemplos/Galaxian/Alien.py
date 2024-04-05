from random import randint

from Animation import Animation
from Utils import bz

from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Alien(Sprite):
    # inicializamos el Alien
    def __init__(self, x, y, images_path, get_target):
        super().__init__(x, y, layer=1, tipo="Alien")

        # iniciador y receptor de colisiones
        self.setCollisionFlag(self.COLLISION_INITIATOR + self.COLLISION_RECEIVER)

        self.animator = Animator(images_path, speed=0.4)
        image_path = self.animator.start()
        self.setShape(image_path)

        self.get_target = get_target
        self.attacking = False
        self.path = None

    # manejamos la actualizacion
    def onUpdate(self, dt, dt_optimal):
        # su forma
        image_path = self.animator.next()
        if image_path:
            self.setShape(image_path)

        # si no está atacando vemos si iniciamos un ataque
        if not self.attacking:
            # si la nave espacial fue destruida nada hacemos
            target = self.get_target()
            if not target:
                return
            tx, ty = target

            # el ataque se inicia de manera aleatoria
            if randint(0, 2000) != 25:
                return

            # la curva de ataque está dada por una curva bezier
            x, y = self.getPosition()
            ww = self.gw.getWidth()
            dx = 400
            if x < ww / 2:
                dx = -dx
            self.path = bz([(x, y), (tx + dx, ty), (tx - dx, ty), (tx, ty)], n=200)
            self.path = self.path + bz(
                [(tx, ty), (x - dx, y), (x + dx, y), (x, y)], n=200
            )
            self.attacking = True

        # en la curva de ataque
        x, y = self.path.pop(0)
        self.setPosition(x, y)

        # verificamos si habrá un próximo movimiento
        if len(self.path) == 0:
            self.attacking = False
            self.path = None

    # manejamos las colisiones
    def onCollision(self, dt, dt_optimal, gobj):
        tipo = gobj.getTipo()
        if tipo in ["Bullet", "SpaceShip"]:
            x, y = self.getPosition()
            self.delete()
            Animation(
                x - 4, y - 4, "Recursos/AlienExplosion-*.png", speed=0.1, duration=0.4
            )
