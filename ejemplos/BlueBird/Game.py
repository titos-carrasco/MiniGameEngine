# VSCODE
# File -> Preferences -> Settings: Buscar y Marcar "Python: Execute In File Dir"

import random
from MiniGameEngine import GameWorld
from MiniGameEngine import TextObject
from BlueBird import BlueBird


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(800, 440, title="Monedas", bgPath="Recursos/Fondo.png")
        self.statusBar = TextObject(
            10, 10, "", font="Arial", size=15, bold=False, italic=False, color="red"
        )

        for i in range(100):
            x = 10 + random.random() * 700
            y = 40 + random.random() * 400
            BlueBird(x, y)

    def onUpdate(self, dt):
        fps = round(1 / dt, 1)
        self.statusBar.setText(text=str(fps))
        if self.isPressed("Escape"):
            self.exitGame()


# -- show time
game = Game()
game.gameLoop(60)
