import cProfile

from Heroe import Heroe
from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.Text import Text
from MiniGameEngine.Box import Box


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(
            800,
            576,
            title="Platformer",
            bg_color="light blue",
            bg_path="Recursos/Tiled/Mundo.png",
            world_size=(3840, 576),
        )

        # para mostrar los FPS dentro de la cámara
        self.status_bar = Text(
            10,
            10,
            layer=100,
            text="      fps",
            font="Arial 10",
            color="black",
        )
        self.getCamera().addGameObject(self.status_bar)

        # el heroe
        self.heroe = Heroe(0, 414)
        self.getCamera().setTarget(self.heroe)

        # el terreno
        suelo = Box(0, 450, 3840, 10, 1, "Suelo", line_width=1, line_color="red")
        suelo.setCollisions(True)

        # un muro con suelo en la parte superior
        muro = Box(192, 388, 64, 62, 1, "Muro", line_width=1, line_color="red")
        muro.setCollisions(True)

        suelo = Box(192, 284, 64, 4, 1, "Suelo", line_width=1, line_color="red")
        suelo.setCollisions(True)

        # los FPS en promedio
        self.prom = [1] * 60

    def onUpdate(self, dt):
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
cProfile.run("game.gameLoop(60,)", sort="cumtime")
