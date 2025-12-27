from Tronco import Tronco
from Vehiculo import Vehiculo
from Rana import Rana
from MiniGameEngine.GameWorld import GameWorld


class Game(GameWorld):
    def __init__(self):
        super().__init__(640, 730, title="Frogger", bg_path="Recursos/Fondo.png")

        # agregamos a los actores
        Tronco(0, 146, 1, "2", "R", 80)
        # Tronco(160, 146, 1, "2", "R", 80)
        # Tronco(320, 146, 1, "2", "R", 80)
        Tronco(480, 146, 1, "2", "R", 80)
        # Tronco(640, 146, 1, "1", "L", 80)

        Tronco(0, 235, 1, "3", "R", 80)
        Tronco(480, 235, 1, "3", "R", 80)

        Tronco(0, 280, 1, "1", "L", 80)
        # Tronco(160, 280, 1, "1", "L", 80)
        Tronco(320, 280, 1, "1", "L", 80)
        # Tronco(480, 280, 1, "1", "L", 80)
        Tronco(640, 280, 1, "1", "L", 80)

        Vehiculo(0, 430, 1, "Camion", "L", 80)
        Vehiculo(160, 430, 1, "Camion", "L", 80)
        Vehiculo(320, 430, 1, "Camion", "L", 80)
        Vehiculo(480, 430, 1, "Camion", "L", 80)
        Vehiculo(640, 430, 1, "Camion", "L", 80)

        Vehiculo(0, 500, 1, "AutoCarrera", "R", 100)
        Vehiculo(160, 500, 1, "Tractor", "R", 100)
        Vehiculo(320, 500, 1, "AutoCarrera", "R", 100)
        Vehiculo(480, 500, 1, "Tractor", "R", 100)
        Vehiculo(640, 500, 1, "AutoCarrera", "R", 100)

        Vehiculo(50 + 0, 580, 1, "Auto", "L", 100)
        Vehiculo(50 + 160, 580, 1, "Auto", "L", 100)
        Vehiculo(50 + 320, 580, 1, "Auto", "L", 100)
        Vehiculo(50 + 480, 580, 1, "Auto", "L", 100)
        Vehiculo(50 + 640, 580, 1, "Auto", "L", 100)

        Rana(300, 644, 2, speed=200)


    def onUpdate(self, dt, dt_optimal):
        if self.isPressed("Escape"):
            self.exitGame()


# -- show time
game = Game()
game.gameLoop(60)
