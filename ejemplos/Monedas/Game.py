# VSCODE
# File -> Preferences -> Settings: Buscar y Marcar "Python: Execute In File Dir"

from MiniGameEngine import GameWorld
from MiniGameEngine import TextObject
from Betty import Betty
from Moneda import Moneda


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(800, 600, title="Monedas", bgpic="Recursos/Fondo.png")
        self.statusBar = TextObject(
            10, 10, "", font="Arial", size=15, bold=False, italic=False, color="black"
        )

        # agregamos a los actores
        Moneda(300, 460)
        Moneda(500, 460)
        Betty(200, 474)

    def onUpdate(self, dt):
        fps = round(1 / dt, 1)
        self.statusBar.setText(text=str(fps))
        if self.isPressed("Escape"):
            self.exitGame()


# -- show time
game = Game()
game.gameLoop(60)
