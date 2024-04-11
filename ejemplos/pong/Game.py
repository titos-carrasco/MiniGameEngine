import random

from Human import Human
from Paleta import Paleta
from Ball import Ball


from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.Text import Text
from MiniGameEngine.Sprite import Sprite


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(640, 384, title="Pong", bg_color="black", debug="F12")

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

        # el puntaje
        self.puntaje1 = 0
        self.puntaje1_text = Text(
            200,
            20,
            layer=100,
            tipo="StatusBar",
            text="",
            font=("Courier", 60, "bold"),
            color="white",
        )

        self.puntaje2 = 0
        self.puntaje2_text = Text(
            350,
            20,
            layer=100,
            tipo="StatusBar",
            text="",
            font=("Courier", 60, "bold"),
            color="white",
        )

        # la franja del centro
        Sprite(316, 22, layer=1, tipo="decor", image_path="Recursos/FranjaCentral.png")

        # las paletas
        self.player1 = Paleta(40, 160)
        self.player2 = Human(600, 160)

        # los FPS en promedio
        self.prom = [1 / 60] * 60

        # para controlar el juego
        self.playing = False

    def onUpdate(self, dt, dt_optimal):
        # mostramos los FPS
        self.prom.pop()
        self.prom.insert(0, dt)
        fps = sum(self.prom) / len(self.prom)
        fps = round(1 / fps, 1)
        self.status_bar.setText(text=f"{fps:5.1f} fps")

        # mostramos el puntaje
        self.puntaje1_text.setText(text=f"{self.puntaje1:02d}")
        self.puntaje2_text.setText(text=f"{self.puntaje2:02d}")

        # abortamos el juego
        if self.isPressed("Escape"):
            self.exitGame()

        # lanzamos una pelota
        elif not self.playing and self.isPressed("space"):
            self.playing = True
            speed_x = random.choice([-200, 200])
            speed_y = random.choice([-200, 200])
            y = random.randint(30, self.getHeight() - 30)
            self.ball = Ball(self.getWidth() / 2, y, speed_x, speed_y)
            self.player1.play()

    # para saber cuando la pelota desaparece de pantalla
    def out(self, donde):
        self.playing = False
        self.player1.stop()
        self.ball = None
        if donde < 0:
            self.puntaje2 = self.puntaje2 + 1
        else:
            self.puntaje1 = self.puntaje1 + 1

    # para informar la posición de la pelota
    def getBallPosition(self):
        return self.ball.getPosition()


# -- show time
game = Game()
game.gameLoop(60)
