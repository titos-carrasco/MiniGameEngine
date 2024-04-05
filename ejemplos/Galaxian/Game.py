from SpaceShip import SpaceShip
from Space import Space
from Alien import Alien

from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.Text import Text


class Game(GameWorld):
    def __init__(self):
        super().__init__(640, 480, title="Galaxian", debug="F12")

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

        # agregamos a los actores
        self.space_ship = SpaceShip(307, 400)

        Space()
        for i in range(2):
            Alien(288 + i * 40, 60, "Recursos/Alien0-*.png", self.getTarget)
        for i in range(6):
            Alien(208 + i * 40, 100, "Recursos/Alien2-*.png", self.getTarget)
        for i in range(8):
            Alien(168 + i * 40, 100 + 40, "Recursos/Alien1-*.png", self.getTarget)
        for i in range(10):
            Alien(128 + i * 40, 100 + 40 * 2, "Recursos/Alien3-*.png", self.getTarget)
            Alien(128 + i * 40, 100 + 40 * 3, "Recursos/Alien3-*.png", self.getTarget)
            Alien(128 + i * 40, 100 + 40 * 4, "Recursos/Alien3-*.png", self.getTarget)

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

    # utilizada por los alien para obtener las coordenadas del target
    def getTarget(self):
        if self.space_ship.isAlive():
            return self.space_ship.getPosition()
        return None


# -- show time
game = Game()
game.gameLoop(60)
