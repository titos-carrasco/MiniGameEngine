from SpaceShip import SpaceShip
from Alien import Alien
from Space import Space
from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.Text import Text


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(800, 600, title="Aliens", debug="F12")

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

        # el espacio infinito
        Space()

        # agregamos a los actores
        SpaceShip(400, 540)
        Alien(80, 50)
        Alien(180, 50)
        Alien(280, 50)
        Alien(380, 50)
        Alien(480, 50)
        Alien(580, 50)
        Alien(680, 50)

        # los FPS en promedio
        self.prom = [1 / 60] * 60

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
