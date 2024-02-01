# VSCODE
# File -> Preferences -> Settings: Buscar y Marcar "Python: Execute In File Dir"

from MiniGameEngine import GameWorld
from MiniGameEngine import TextObject
from Betty import Betty
from Moneda import Moneda


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(800, 600, title="Monedas", bgPath="Recursos/Fondo.png")
        self.statusBar = TextObject(
            10, 10, "", font="Arial", size=15, bold=False, italic=False, color="black"
        )

        # agregamos a los actores
        Betty(200, 474, layer=2)
        Moneda(300, 460, layer=1)
        Moneda(500, 460, layer=3)

    def onUpdate(self, dt):
        fps = round(1 / dt, 1)
        self.statusBar.setText(text=str(fps))
        if self.isPressed("Escape"):
            self.exitGame()


# -- show time
game = Game()
game.gameLoop(60)
