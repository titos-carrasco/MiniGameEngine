from SpaceShip import SpaceShip
from Alien import Alien
from Space import Space
from MiniGameEngine.Text import Text
from MiniGameEngine.GameWorld import GameWorld


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(800, 600, title="Aliens", key_debug="F12")
        self.gw = GameWorld._getInstance()

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
        Space(layer=1)

        # agregamos a los actores
        SpaceShip(400, 540, layer=2)
        Alien(80, 50, layer=2)
        Alien(180, 50, layer=2)
        Alien(280, 50, layer=2)
        Alien(380, 50, layer=2)
        Alien(480, 50, layer=2)
        Alien(580, 50, layer=2)
        Alien(680, 50, layer=2)

    def onUpdate(self, _dt, _dt_optimal):
        if self.isPressed("Escape"):
            self.exitGame()
        fps = self.gw.getFPS()
        self.status_bar.setText(text=f"{fps:5.1f} fps")


# -- show time
game = Game()
game.gameLoop(60)
