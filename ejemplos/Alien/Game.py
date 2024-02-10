from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.Text import Text

from SpaceShip import SpaceShip
from Alien import Alien


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(800, 600, title="Aliens", bgPath="Recursos/Fondo.png")

        # para mostrar los FPS
        self.statusBar = Text(
            10,
            10,
            layer=100,
            text="60",
            font="Arial",
            size=10,
            bold=False,
            italic=False,
            color="white",
        )

        # agregamos a los actores
        SpaceShip(400, 540)
        Alien(80, 50)
        Alien(180, 50)
        Alien(280, 50)
        Alien(380, 50)
        Alien(480, 50)
        Alien(580, 50)
        Alien(680, 50)

    def onUpdate(self, dt):
        fps = round(1 / dt, 1)
        self.statusBar.setText(text="%5.1f fps" % fps)
        if self.isPressed("Escape"):
            self.exitGame()


# -- show time
game = Game()
game.gameLoop(60)
