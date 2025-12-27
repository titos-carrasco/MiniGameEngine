import random
import time
import cProfile
from BlueBird import BlueBird
from MiniGameEngine.Text import Text
from MiniGameEngine.GameWorld import GameWorld


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(
            800, 440, title="Blue Bird", bg_path="Recursos/Fondo.png", key_debug="F12"
        )
        self.gw = GameWorld._getInstance()

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

        # para detener el juego en un lapso de tiempo específico
        self.t = time.time()

    def onUpdate(self, dt, dt_optimal):
        if self.isPressed("Escape"):
            self.exitGame()
        fps = self.gw.getFPS()
        self.status_bar.setText(text=f"{fps:5.1f} fps")

        t = time.time()
        if t - self.t > 20:
            self.exitGame()


# -- show time
game = Game()
# game.gameLoop(60)
cProfile.run("game.gameLoop(60)", sort="cumtime")
