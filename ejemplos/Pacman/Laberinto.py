from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.EmptyObject import EmptyObject


class Laberinto(Sprite):
    def __init__(self, x, y, layer):
        super().__init__(
            x, y, image_path="./Recursos/Laberinto.png", layer=layer, tipo="Laberinto"
        )

        # fmt: off
        dots = [
            "............BB............",
            ".BBBB.BBBBB.BB.BBBBB.BBBB.",
            "CBBBB.BBBBB.BB.BBBBB.BBBBC",
            ".BBBB.BBBBB.BB.BBBBB.BBBB.",
            "..........................",
            ".BBBB.BB.BBBBBBBB.BB.BBBB.",
            ".BBBB.BB.BBBBBBBB.BB.BBBB.",
            "......BB....BB....BB......",
            "BBBBB.BBBBBBBBBBBBBB.BBBBB",
            "BBBBB.BBBBBBBBBBBBBB.BBBBB",
            "BBBBB.BBBBBBBBBBBBBB.BBBBB",
            "BBBBB.BBBBBBBBBBBBBB.BBBBB",
            "BBBBB.BBBBBBBBBBBBBB.BBBBB",
            "BBBBB.BBBBBBBBBBBBBB.BBBBB",
            "BBBBB.BBBBBBBBBBBBBB.BBBBB",
            "BBBBB.BBBBBBBBBBBBBB.BBBBB",
            "BBBBB.BBBBBBBBBBBBBB.BBBBB",
            "BBBBB.BBBBBBBBBBBBBB.BBBBB",
            "BBBBB.BBBBBBBBBBBBBB.BBBBB",
            "............BB............",
            ".BBBB.BBBBB.BB.BBBBB.BBBB.",
            ".BBBB.BBBBB.BB.BBBBB.BBBB.",
            "C..BB.......BB.......BB..C",
            "BB.BB.BB.BBBBBBBB.BB.BB.BB",
            "BB.BB.BB.BBBBBBBB.BB.BB.BB",
            "......BB....BB....BB......",
            ".BBBBBBBBBB.BB.BBBBBBBBBB.",
            ".BBBBBBBBBB.BB.BBBBBBBBBB.",
            ".........................."
        ]
        # fmt: on
        muros = [
            (0, 48, 464, 16),
            (0, 64, 16, 208),
            (0, 304, 16, 240),
            (0, 544, 464, 16),
            (448, 304, 16, 240),
            (448, 64, 16, 208),
            (48, 96, 48, 32),
            (128, 96, 64, 32),
            (224, 64, 16, 64),
            (272, 96, 64, 32),
            (368, 96, 48, 32),
            (48, 160, 48, 16),
            (128, 160, 16, 112),
            (176, 160, 112, 16),
            (320, 160, 16, 112),
            (368, 160, 48, 16),
            (16, 208, 80, 64),
            (144, 208, 48, 16),
            (224, 176, 16, 48),
            (272, 208, 48, 16),
            (368, 208, 81, 64),
            (176, 256, 112, 64),
            (16, 304, 80, 64),
            (128, 304, 16, 64),
            (176, 352, 112, 16),
            (320, 304, 16, 64),
            (368, 304, 80, 64),
            (48, 400, 48, 16),
            (128, 400, 64, 16),
            (224, 368, 16, 48),
            (272, 400, 64, 16),
            (368, 400, 48, 16),
            (16, 448, 32, 16),
            (80, 416, 16, 48),
            (128, 448, 16, 48),
            (176, 448, 112, 16),
            (320, 448, 16, 48),
            (368, 416, 16, 48),
            (416, 448, 32, 16),
            (48, 496, 144, 16),
            (224, 464, 16, 48),
            (272, 496, 144, 16),
        ]

        for muro in muros:
            x, y, w, h = muro
            Muro(x, y, w, h, 2)

        y = 5 * 16
        for row in dots:
            x = 32
            for b in row:
                if b == ".":
                    Dot(x, y, 2)
                elif b == "C":
                    Circle(x - 6, y - 6, 2)
                x = x + 16
            y = y + 16


class Muro(EmptyObject):
    def __init__(self, x, y, w, h, layer):
        super().__init__(x, y, width=w, height=h, layer=layer, tipo="Muro", debug=True)
        self.setCollisionFlag(self.COLLISION_RECEIVER)


class Dot(Sprite):
    def __init__(self, x, y, layer):
        super().__init__(
            x, y, image_path="./Recursos/Dot.png", layer=layer, tipo="Punto"
        )
        self.setCollisionFlag(self.COLLISION_RECEIVER)


class Circle(Sprite):
    def __init__(self, x, y, layer):
        super().__init__(
            x, y, image_path="./Recursos/Circle.png", layer=layer, tipo="Circulo"
        )
        self.setCollisionFlag(self.COLLISION_RECEIVER)
