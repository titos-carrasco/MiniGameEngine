from SpaceShip import SpaceShip
from Asteroid import Asteroid
from MiniGameEngine.Text import Text
from MiniGameEngine.GameWorld import GameWorld


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(800, 600, title="Asteroids", bg_color="black", key_debug="F12")
        self.gw = GameWorld._getInstance()

        # para mostrar los FPS
        self.status_bar = Text(10, 10, layer=100, tipo="StatusBar", text=" 60.0 fps", font="Arial 10", color="white")

        # número de asteroides
        self.count = 10

        # agregamos a los actores
        SpaceShip(400, 300, layer=2)
        for _i in range(self.count):
            Asteroid(layer=2)

    def message(self, msg, _gobj):
        if msg == "Asteroide Out":
            Asteroid(layer=2)

    def onUpdate(self, _dt, _dt_optimal):
        if self.isPressed("Escape"):
            self.exitGame()
        fps = self.gw.getFPS()
        self.status_bar.setText(text=f"{fps:5.1f} fps")


# -- show time
game = Game()
game.gameLoop(60)
