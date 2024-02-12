from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.Text import Text

from Betty import Betty
from Moneda import Moneda


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(800, 600, title="Monedas", bg_path="Recursos/Fondo.png")
        self.statusBar = Text(
            10,
            10,
            layer=100,
            text="60",
            font="Arial 12",
            color="black",
        )

        # agregamos a los actores
        Betty(200, 456, layer=2)
        Moneda(300, 440, layer=3)
        Moneda(500, 440, layer=1)

    def onUpdate(self, dt):
        fps = round(1 / dt, 1)
        self.statusBar.setText(text="%5.1f fps" % fps)
        if self.isPressed("Escape"):
            self.exitGame()


# -- show time
game = Game()
game.gameLoop(60)
