from Heroe import Heroe
from Coin import Coin
from Base import Base
from Escalera import Escalera

from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.EmptyObject import EmptyObject
from MiniGameEngine.Text import Text


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(
            800,
            576,
            title="Platformer",
            bg_color="light blue",
            bg_path="Recursos/Map/Mundo.png",
            world_size=(3840, 576),
            debug="F12",
        )

        # para mostrar los FPS dentro de la cámara
        self.status_bar = Text(
            10,
            10,
            layer=100,
            tipo="StatusBar",
            text="      fps",
            font=("Courier New", 10),
            color="black",
            debug=False,
        )
        self.getCamera().addGameObject(self.status_bar)

        # el heroe
        self.heroe = Heroe(600, 100)
        self.getCamera().setTarget(self.heroe)

        # el terreno
        suelo = EmptyObject(0, 448, 3840, 8, 1, "Suelo", debug=True)
        suelo.setCollisionFlag(suelo.COLLISION_RECEIVER)

        # un muro con suelo en la parte superior
        self.muro = EmptyObject(192, 390, 64, 58, 1, "Muro", debug=True)
        suelo.setCollisionFlag(suelo.COLLISION_RECEIVER)

        suelo = EmptyObject(192, 384, 64, 8, 1, "Suelo", debug=True)
        suelo.setCollisionFlag(suelo.COLLISION_RECEIVER)

        # una moneda bien arriba
        Coin(350, 100)

        # algunas bases móviles
        Base(300, 260, 1, distance_y=70, vy=90)
        Base(600, 300, 1, distance_x=120, vx=90)

        # algunas escaleras
        Escalera(800, 320)

        # la prioridad en los eventos onUpdate y onCollision
        self.setPriority("Base", "Heroe", "Suelo")

        # los FPS en promedio
        self.prom = [1] * 60

    def onUpdate(self, dt, dt_optimal):
        # mostramos los FPS
        self.prom.pop()
        self.prom.insert(0, dt)
        fps = sum(self.prom) / len(self.prom)
        fps = round(1 / fps, 1)
        self.status_bar.setText(text=f"{fps:5.1f} fps")

        # verificamos si debemos abortar el juego
        if self.isPressed("Escape"):
            self.exitGame()


# -- show time
game = Game()
game.gameLoop(60)
