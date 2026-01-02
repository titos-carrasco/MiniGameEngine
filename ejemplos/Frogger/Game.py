from Tronco import Tronco
from Vehiculo import Vehiculo
from Rana import Rana
from MiniGameEngine.Text import Text
from MiniGameEngine.GameWorld import GameWorld


class Game(GameWorld):
    def __init__(self):
        super().__init__(640, 730, title="Frogger", bg_path="Recursos/Fondo.png")
        self.gw = GameWorld._getInstance()

        # para mostrar los FPS
        self.status_bar = Text(
            10,
            10,
            layer=100,
            tipo="StatusBar",
            text=" 60.0 fps",
            font="Arial 10",
            color="white",
        )

        # agregamos a los actores
        Tronco(0, 146, 1, "2", "R", 80)
        Tronco(480, 146, 1, "2", "R", 80)
        Tronco(0, 235, 1, "3", "R", 80)
        Tronco(480, 235, 1, "3", "R", 80)
        Tronco(0, 280, 1, "1", "L", 80)
        Tronco(320, 280, 1, "1", "L", 80)
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

        Rana(300, 644, 2, speed=150)

    def onUpdate(self, _dt, _dt_optimal):
        if self.isPressed("Escape"):
            self.exitGame()
        fps = self.gw.getFPS()
        self.status_bar.setText(text=f"{fps:5.1f} fps")


# -- show time
game = Game()
game.gameLoop(60)
