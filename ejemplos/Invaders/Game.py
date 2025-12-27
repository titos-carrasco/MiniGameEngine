from Base import Base
from Invader import Invader
from Torre import Torre
from MiniGameEngine.Text import Text
from MiniGameEngine.GameWorld import GameWorld


class Game(GameWorld):
    def __init__(self):
        super().__init__(640, 480, title="Invaders", bg_color="black", key_debug="F12")
        self.gw = GameWorld._getInstance()
        self.puntaje = 0

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
        x0 = 90
        x = 140
        y = 80
        d = 30
        for x in range(11):
            Invader(x0 + 2 + x * 30, y + d * 0, "Recursos/Invader1-*.png")
            Invader(x0 + x * 30, y + d * 1, "Recursos/Invader2-*.png")
            Invader(x0 + x * 30, y + d * 2, "Recursos/Invader2-*.png")
            Invader(x0 + x * 30, y + d * 3, "Recursos/Invader3-*.png")
            Invader(x0 + x * 30, y + d * 4, "Recursos/Invader3-*.png")

        for x in range(4):
            Torre(120 + x * 110, 340)

        Base(294, 400)

    def onUpdate(self, dt, dt_optimal):
        if self.isPressed("Escape"):
            self.exitGame()
        fps = self.gw.getFPS()
        self.status_bar.setText(text=f"{fps:5.1f} fps")

        # self.status_bar_points.setText(text=f"{self.puntaje:03d}")

    def addPoints(self, points):
        self.puntaje = self.puntaje + points


# -- show time
game = Game()
game.gameLoop(60)
