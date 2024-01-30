# VSCODE
# File -> Preferences -> Settings: Buscar y Marcar "Python: Execute In File Dir"

from MiniGameEngine import GameWorld
from BlueBird import BlueBird


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(800, 440, title="Monedas", bgpic="Recursos/Fondo.png")

        BlueBird(400, 300)

    def onUpdate(self, dt):
        if self.isPressed("Escape"):
            self.exitGame()


# -- show time
game = Game()
game.gameLoop(60)
