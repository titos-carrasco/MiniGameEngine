import random

from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.Text import Text

from BlueBird import BlueBird


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(800, 440, title="Blue Bird", bgPath="Recursos/Fondo.png")

        # para mostrar los FPS
        self.statusBar = Text(
            2,
            2,
            layer=100,
            text="60",
            font="Arial",
            size=12,
            bold=False,
            italic=False,
            color="black",
        )

        for i in range(30):
            x = random.randint(-40, 700)
            y = random.randint(20, 400)
            BlueBird(x, y)

    def onUpdate(self, dt):
        fps = round(1 / dt, 1)
        self.statusBar.setText(text="%5.1f fps" % fps)
        if self.isPressed("Escape"):
            self.exitGame()


# -- show time
game = Game()
game.gameLoop(60)
