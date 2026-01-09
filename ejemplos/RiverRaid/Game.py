from Avion import Avion
from Puente import Puente
from Barco import Barco
from Helicoptero import Helicoptero
from MiniGameEngine.Text import Text
from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.EmptyObject import EmptyObject


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(
            304,
            480,
            title="River Raid",
            bg_color="black",
            bg_path="./Recursos/Escenario-01.png",
            world_size=(304, 1175),
            key_debug="F12",
        )
        self.gw = GameWorld._getInstance()
        self.cam = self.getCamera()

        self.status_bar = Text(
            10,
            10,
            layer=100,
            tipo="StatusBar",
            text=" 60.0 fps",
            font="Arial 10",
            color="white",
        )
        self.cam.addGameObject(self.status_bar)
        self.avion = Avion(137, 1100, layer=3, speed=1)  # 1100
        self.cam.setPosition(0, 695)  # 695
        Puente(112, 9, layer=3)
        Barco(126, 972, 3, "R", self.gw)
        Helicoptero(115, 903, 3, "L", self.gw)
        Helicoptero(97, 680, 3, "R", self.gw)
        Helicoptero(127, 616, 3, "L", self.gw)

        colisionadores = [
            (0, 988, 112, 188),
            (176, 988, 128, 187),
            (0, 63, 72, 925),
            (216, 63, 88, 925),
            (0, 0, 112, 63),
            (176, 0, 127, 63),
        ]
        for coords in colisionadores:
            obj = EmptyObject(*coords, layer=4, tipo="Tierra", debug=False)
            obj.setCollisionFlag(obj.COLLISION_RECEIVER)

        self.running = True
        self.avion.start()

    def onUpdate(self, _dt, _dt_optimal):
        if self.isPressed("Escape"):
            self.exitGame()
        fps = self.gw.getFPS()
        self.status_bar.setText(text=f"{fps:5.1f} fps")

        if not self.running:
            return

        if not self.avion.running:
            return

        x, y = self.cam.getPosition()
        if y > -50:
            self.cam.setPosition(x, y - 1)


# -- show time
game = Game()
game.gameLoop(60)
