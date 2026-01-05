from Laberinto import Laberinto
from Pacman import Pacman
from Blinky import Blinky
from MiniGameEngine.Text import Text
from MiniGameEngine.GameWorld import GameWorld


class Game(GameWorld):
    def __init__(self):
        super().__init__(464, 592, title="Pacman", key_debug="F12")
        self.gw = GameWorld._getInstance()

        # el laberinto
        self.laberinto = Laberinto(0, 0, 1)

        # para mostrar los FPS
        self.status_bar = Text(
            30,
            20,
            layer=100,
            tipo="StatusBar",
            text=" 60.0 fps",
            font="Arial 10",
            color="white",
        )

        # los puntos
        self.puntos = 0
        self.point_bar = Text(
            360,
            10,
            layer=100,
            tipo="StatusBar",
            text="0000",
            font="Arial 20",
            color="white",
        )


        # agregamos a los actores
        Pacman(13 * 16 + 8, 320, 10, self)
        Blinky(12*16, 17*16, 10)

    def onUpdate(self, _dt, _dt_optimal):
        if self.isPressed("Escape"):
            self.exitGame()
        fps = self.gw.getFPS()
        self.status_bar.setText(text=f"{fps:5.1f} fps")

    def eatDot(self):
        self.puntos = self.puntos + 1
        self.point_bar.setText(f"{self.puntos:04d}")


# -- show time
game = Game()
game.gameLoop(60)
