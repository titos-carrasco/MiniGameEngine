from Heroe import Heroe
from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.Text import Text
from MiniGameEngine.Box import Box

from Coin import Coin
from Base import Base


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(
            800,
            576,
            title="Platformer",
            bg_color="light blue",
            bg_path="Recursos/Map/Mundo.png",
            world_size=(3840, 576),
        )

        # para mostrar los FPS dentro de la cámara
        self.status_bar = Text(
            10,
            10,
            layer=100,
            tipo ="FPS",
            text="      fps",
            font=("Courier New", 10),
            color="black",
            debug=False,
        )
        self.getCamera().addGameObject(self.status_bar)

        # el heroe
        self.heroe = Heroe(300, 100)
        self.getCamera().setTarget(self.heroe)

        # el terreno
        suelo = Box(0, 448, 3840, 8, 1, "Suelo", border=0, debug=True)
        suelo.setCollisions(True)
        suelo.setPosition(0, 448)

        # un muro con suelo en la parte superior
        self.muro = Box(192, 390, 64, 58, 1, "Muro", border=0, debug=True)
        self.muro.setCollisions(True)

        suelo = Box(192, 384, 64, 8, 1, "Suelo", border=0, debug=True)
        suelo.setCollisions(True)

        # una moneda bien arriba
        coin = Coin(350, 100)

        # una base movil para alcanzar la moneda
        base = Base(300, 300)

        # la prioridad en los eventos onUpdate y onCollision
        self.setPriority("Base", "Suelo", "Heroe")

        # los FPS en promedio
        self.prom = [1] * 60

    def onUpdate(self, dt, dt_optimal):
        # mostramos los FPS
        self.prom.pop()
        self.prom.insert(0, dt)
        fps = sum(self.prom) / len(self.prom)
        fps = round(1 / fps, 1)
        self.status_bar.setText(text=f"{fps:5.1f} fps")

        # verificamos si debemos abortar el juego
        if self.isPressed("Escape"):
            self.exitGame()


# -- show time
game = Game()
game.gameLoop(60)
