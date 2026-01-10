from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Text import Text


class Tablero(Sprite):
    def __init__(self, x, y, layer, gw):
        super().__init__(
            x, y, layer=layer, tipo="Tablero", image_path="./Recursos/Tablero.png"
        )
        self.points = Text(
            x + 130,
            y,
            layer=layer + 1,
            tipo="Puntos",
            text="00000",
            font="Arial 10",
            color="yellow",
        )
        gw.getCamera().addGameObject(self.points)

    def showPoints(self, points):
        self.points.setText(f"{points:05d}")
