from Betty import Betty
from Moneda import Moneda
from MiniGameEngine.Text import Text
from MiniGameEngine.GameWorld import GameWorld


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(800, 600, title="Monedas", bg_path="Recursos/Fondo.png", key_debug="F12")
        self.gw = GameWorld._getInstance()

        # para mostrar los FPS
        self.status_bar = Text(10, 10, layer=100, tipo="StatusBar", text=" 60.0 fps", font="Arial 12", color="black")

        # agregamos a los actores
        Betty(200, 456, layer=2)
        Moneda(300, 440, layer=3)
        Moneda(500, 440, layer=1)

    def onUpdate(self, _dt, _dt_optimal):
        if self.isPressed("Escape"):
            self.exitGame()
        fps = self.gw.getFPS()
        self.status_bar.setText(text=f"{fps:5.1f} fps")


# -- show time
game = Game()
game.gameLoop(60)
