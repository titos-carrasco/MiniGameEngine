from Base import Base
from Invader import Invader
from Torre import Torre

from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.Text import Text


class Game(GameWorld):
    def __init__(self):
        super().__init__(640, 480, title="Invaders", bg_color="black", debug="F12")

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
        x = 140
        y = 80
        d = 30
        for x in range(11):
            Invader(92 + x * 30, y + d * 0, "Recursos/Invader1-*.png")
            Invader(90 + x * 30, y + d * 1, "Recursos/Invader2-*.png")
            Invader(90 + x * 30, y + d * 2, "Recursos/Invader2-*.png")
            Invader(90 + x * 30, y + d * 3, "Recursos/Invader3-*.png")
            Invader(90 + x * 30, y + d * 4, "Recursos/Invader3-*.png")

        for x in range(4):
            Torre(120 + x * 110, 340)

        Base(294, 400)

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
