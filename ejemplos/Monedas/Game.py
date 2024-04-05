from Betty import Betty
from Moneda import Moneda
from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.Text import Text


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(
            800, 600, title="Monedas", bg_path="Recursos/Fondo.png", debug="F12"
        )
        self.status_bar = Text(
            10,
            10,
            layer=100,
            tipo="StatusBar",
            text=" 60.0 fps",
            font="Arial 12",
            color="black",
        )

        # agregamos a los actores
        Betty(200, 456, layer=2)
        Moneda(300, 440, layer=3)
        Moneda(500, 440, layer=1)

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
