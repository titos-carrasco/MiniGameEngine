from Avion import Avion
from Puente import Puente
from Barco import Barco
from Helicoptero import Helicoptero
from Tablero import Tablero
from MiniGameEngine.Text import Text
from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.EmptyObject import EmptyObject


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(
            608,
            720,
            title="River Raid",
            bg_color="black",
            bg_path="./Recursos/Escenario-01.png",
            world_size=(608, 2350),
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

        self.tablero = Tablero(0, 720 - 84, layer=100, gw=self.gw)
        self.cam.addGameObject(self.tablero)

        self.points = 0

        self.avion = Avion(274, 2200, layer=3, speed=1.4)  # 1100
        self.cam.setPosition(0, 2350 - 720)  # world height - win height
        Puente(112*2, 9*2, layer=3, gw=self.gw)
        Barco(126*2, 972*2, 3, "R", self.gw)
        Helicoptero(115*2, 903*2, 3, "L", self.gw)
        Helicoptero(97*2, 680*2, 3, "R", self.gw)
        Helicoptero(127*2, 616, 3, "L", self.gw)

        colisionadores = [
            (0, 988*2, 112*2, 188*2),
            (176*2, 988*2, 128*2, 187*2),
            (0, 63*2, 72*2, 925*2),
            (216*2, 63*2, 88*2, 925*2),
            (0, 0, 112*2, 63*2),
            (176*2, 0, 127*2, 63*2),
        ]
        for coords in colisionadores:
            obj = EmptyObject(*coords, layer=4, tipo="Tierra", debug=False)
            obj.setCollisionFlag(obj.COLLISION_RECEIVER)

        self.running = False
        # self.avion.start()

    def onUpdate(self, _dt, _dt_optimal):
        if self.isPressed("Escape"):
            self.exitGame()
        fps = self.gw.getFPS()
        self.status_bar.setText(text=f"{fps:5.1f} fps")

        if not self.running:
            if self.gw.isPressed("space"):
                self.running = True
                self.avion.start()
            return

        if not self.avion.running:
            return

        x, y = self.cam.getPosition()
        if y > 0:
            self.cam.setPosition(x, y - self.avion.speed)

    def addPoints(self, points):
        self.points = self.points + points
        self.tablero.showPoints(self.points)


# -- show time
game = Game()
game.gameLoop(60)
