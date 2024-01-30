# VSCODE
# File -> Preferences -> Settings: Buscar y Marcar "Python: Execute In File Dir"

from MiniGameEngine import GameWorld
from MiniGameEngine import GameText
from SpaceShip import SpaceShip
from Alien import Alien


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(800, 600, title="Actividad 01", bgpic="Recursos/Fondo.png")
        self.status_line = GameText(0, 0, color="white")

        # agregamos a los actores
        SpaceShip(400, 540)
        Alien(100, 50)
        Alien(200, 50)
        Alien(300, 50)
        Alien(400, 50)
        Alien(500, 50)
        Alien(600, 50)
        Alien(700, 50)

    def onUpdate(self, dt):
        fps = round(1 / dt, 1)
        self.status_line.changeText(x=0, y=0, text=str(fps))
        if self.isPressed("Escape"):
            self.exitGame()


# -- show time
game = Game()
game.gameLoop(60)
