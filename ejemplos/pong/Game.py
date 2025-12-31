import random
from Human import Human
from Paleta import Paleta
from Ball import Ball
from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Text import Text
from MiniGameEngine.GameWorld import GameWorld


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(640, 384, title="Pong", bg_color="black", key_debug="F12")
        self.ball = None

        # el puntaje
        self.puntaje1 = 0
        self.puntaje1_text = Text(
            200, 20, layer=100, tipo="StatusBar", text="", font=("Courier", 60, "bold"), color="white"
        )

        self.puntaje2 = 0
        self.puntaje2_text = Text(
            350, 20, layer=100, tipo="StatusBar", text="", font=("Courier", 60, "bold"), color="white"
        )

        # la franja del centro
        Sprite(316, 22, layer=1, tipo="decor", image_path="Recursos/FranjaCentral.png")

        # las paletas
        self.player1 = Paleta(40, 160, layer=1)
        self.player2 = Human(600, 160, layer=1)

        # para controlar el juego
        self.playing = False

    def onUpdate(self, _dt, _dt_optimal):
        if self.isPressed("Escape"):
            self.exitGame()

        # mostramos el puntaje
        self.puntaje1_text.setText(text=f"{self.puntaje1:02d}")
        self.puntaje2_text.setText(text=f"{self.puntaje2:02d}")

        # lanzamos una pelota
        if not self.playing and self.isPressed("space"):
            self.playing = True
            speed_x = random.choice([-200, 200])
            speed_y = random.choice([-200, 200])
            y = random.randint(30, self.getHeight() - 30)
            self.ball = Ball(self.getWidth() / 2, y, 1, speed_x, speed_y)
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
