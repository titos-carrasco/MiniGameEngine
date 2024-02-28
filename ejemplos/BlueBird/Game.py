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
            text=" 60.0 fps",
            font=("Courier New", 12),
            color="red",
        )

        for i in range(30):
            x = random.randint(-40, 700)
            y = random.randint(20, 400)
            BlueBird(x, y)
        self.t = time.time()

    def onUpdate(self, dt):
        fps = round(1 / dt, 1)
        if fps < 59:
            self.status_bar.setText(text=f"             {fps:5.1f} fps")
        else:
            self.status_bar.setText(text=f"{fps:5.1f} fps")

        if self.isPressed("Escape"):
            self.exitGame()

        t = time.time()
        if t - self.t > 10:
            self.exitGame()


# -- show time
game = Game()
# game.gameLoop(60)
cProfile.run("game.gameLoop(60)", sort="cumtime")
