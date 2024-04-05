from Pasto import Pasto
from Perro import Perro
from Pato import Pato
from MiniGameEngine.GameObject import GameWorld
from MiniGameEngine.Text import Text


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(
            720, 375, title="Duck Hunt", bg_path="Recursos/Fondo.png", debug="F12"
        )
        self.status_bar = Text(
            4,
            4,
            layer=100,
            tipo="StatusBar",
            text=" 60.0 fps",
            font="Arial 12",
            color="black",
        )

        # agregamos a los actores
        Pasto(0, 209)
        Perro(0, 270)
        Pato(-200, 80)
        Pato(-130, 60)
        Pato(-60, 40)

        # los FPS en promedio
        self.prom = [1 / 60] * 60

    def onUpdate(self, dt, dt_optimal):
        self.prom.pop()
        self.prom.insert(0, dt)
        fps = sum(self.prom) / len(self.prom)
        fps = round(1 / fps, 1)
        self.status_bar.setText(text=f"{fps:5.1f} fps")

        if self.isPressed("Escape"):
            self.exitGame()


# -- show time
game = Game()
game.gameLoop(60)
