from MiniGameEngine.GameObject import GameWorld
from MiniGameEngine.Text import Text

from Pasto import Pasto
from Perro import Perro
from Pato import Pato


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(720, 375, title="Duck Hunt", bgPath="Recursos/Fondo.png")
        self.statusBar = Text(
            4,
            4,
            layer=100,
            text="60",
            font="Arial",
            size=12,
            bold=False,
            italic=False,
            color="black",
        )

        # agregamos a los actores
        Pasto(0, 209)
        Perro(0, 270)
        Pato(-200, 80)
        Pato(-130, 60)
        Pato(-60, 40)

    def onUpdate(self, dt):
        fps = round(1 / dt, 1)
        self.statusBar.setText(text="%5.1f fps" % fps)
        if self.isPressed("Escape"):
            self.exitGame()


# -- show time
game = Game()
game.gameLoop(60)