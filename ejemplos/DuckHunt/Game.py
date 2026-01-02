from Pasto import Pasto
from Perro import Perro
from Pato import Pato
from MiniGameEngine.Text import Text
from MiniGameEngine.GameObject import GameWorld


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(
            310,
            232,
            title="Duck Hunt",
            bg_path="Recursos/Fondo.png",
            skin={"path": "Recursos/Skin2.png", "x": 15, "y": 14},
        )
        self.gw = GameWorld._getInstance()

        # para mostrar los FPS
        self.status_bar = Text(4, 4, layer=100, tipo="StatusBar", text=" 60.0 fps", font="Arial 12", color="black")

        # agregamos a los actores
        Pasto(0, 150, layer=3)
        Perro(0, 160, layer=4)
        Pato(-200, 30, layer=2)
        Pato(-130, 20, layer=2)
        Pato(-60, 10, layer=2)

    def onUpdate(self, _dt, _dt_optimal):
        if self.isPressed("Escape"):
            self.exitGame()
        fps = self.gw.getFPS()
        self.status_bar.setText(text=f"{fps:5.1f} fps")


# -- show time
game = Game()
game.gameLoop(60)
