from MiniGameEngine import GameWorld
from Pasto import Pasto
from Perro import Perro
from Pato import Pato


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(720, 375, title="Duck Hunt", bgPath="Recursos/Fondo.png")

        # agregamos a los actores
        Pasto(360, 265)
        Perro(50, 300)
        Pato(-200, 80)
        Pato(-130, 60)
        Pato(-60, 40)

    def onUpdate(self, dt):
        if self.isPressed("Escape"):
            self.exitGame()


# -- show time
game = Game()
game.gameLoop(60)
