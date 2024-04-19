from SpaceShip import SpaceShip
from Asteroid import Asteroid

from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.Text import Text


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(800, 600, title="Asteroids", bg_color="black", debug="F12")

        # para mostrar los FPS
        self.status_bar = Text(
            10,
            10,
            layer=100,
            tipo="StatusBar",
            text=" 60.0 fps",
            font="Arial 10",
            color="white",
        )

        # número de asteroides
        self.count = 10

        # agregamos a los actores
        SpaceShip(400, 300)
        for i in range(self.count):
            Asteroid()

        # los FPS en promedio
        self.prom = [1 / 60] * 60

    def message(self, msg, gobj):
        if msg == "Asteroide Out":
            Asteroid()

    def onUpdate(self, dt, dt_optimal):
        self.prom.pop()
        self.prom.insert(0, dt)
        fps = sum(self.prom) / len(self.prom)
        fps = round(1 / fps, 1)
        self.status_bar.setText(text=f"{fps:5.1f} fps")

        if self.isPressed("Escape"):
            self.exitGame()


# -- show time
game = Game()
game.gameLoop(60)
