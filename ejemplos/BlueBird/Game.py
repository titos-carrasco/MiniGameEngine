import random
import time
import cProfile

from BlueBird import BlueBird
from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.Text import Text


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(
            800, 440, title="Blue Bird", bg_path="Recursos/Fondo.png", debug="F12"
        )

        # para mostrar los FPS
        self.status_bar = Text(
            2,
            2,
            layer=100,
            tipo="StatusBar",
            text=" 60.0 fps",
            font=("Courier New", 12),
            color="red",
        )

        # utilizamos una variable llamada "_"
        for _ in range(30):
            x = random.randint(-40, 700)
            y = random.randint(20, 400)
            BlueBird(x, y)

        # los FPS en promedio
        self.prom = [1 / 60] * 60 * 5

        # para detener el juego en un lapso de tiempo específico
        self.t = time.time()

    def onUpdate(self, dt, dt_optimal):
        self.prom.pop()
        self.prom.insert(0, dt)
        pfps = sum(self.prom) / len(self.prom)
        pfps = round(1 / pfps, 1)
        fps = round(1 / dt, 1)
        self.status_bar.setText(text=f"{pfps:5.1f} fps - {fps:5.1f} fps")

        if self.isPressed("Escape"):
            self.exitGame()

        t = time.time()
        if t - self.t > 20:
            self.exitGame()


# -- show time
game = Game()
# game.gameLoop(60)
cProfile.run("game.gameLoop(60)", sort="cumtime")
