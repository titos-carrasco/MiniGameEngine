from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.EmptyObject import EmptyObject


class Laberinto(Sprite):
    def __init__(self, x, y, layer):
        super().__init__(
            x, y, image_path="./Recursos/Laberinto.png", layer=layer, tipo="Laberinto"
        )

        # fmt: off
        self.mapa = [
            "BBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
            "B............ B............ B",
            "B.    .     . B.     .    . B",
            "Bc BBB. BBBB. B. BBBB. BBBc B",
            "B. BBB. BBBB. B. BBBB. BBB. B",
            "B.......................... B",
            "B.    .  .        .  .    . B",
            "B. BBB. B. BBBBBBB. B. BBB. B",
            "B...... B.... B.... B...... B",
            "B     . B   . B.    B.      B",
            "BBBBBB. BBBB. B. BBBB. BBBBBB",
            "BBBBBB. B.......... B. BBBBBB",
            "BBBBBB. B.        . B. BBBBBB",
            "BBBBBB. B. BB   BB. B. BBBBBB",
            ".......... B     B.......... ",
            "      .  . B     B.  .       ",
            "BBBBBB. B. BBBBBBB. B. BBBBBB",
            "BBBBBB. B....  .... B. BBBBBB",
            "BBBBBB. B.        . B. BBBBBB",
            "BBBBBB. B. BBBBBBB. B. BBBBBB",
            "B............ B............ B",
            "B.    .     . B.     .    . B",
            "B. BBB. BBBB. B. BBBB. BBB. B",
            "Bc.. B................ B..c B",
            "B  . B.  .        .  . B.   B",
            "BBB. B. B. BBBBBBB. B. B. BBB",
            "B...... B.... B.... B...... B",
            "B.      B   . B.    B     . B",
            "B. BBBBBBBBB. B. BBBBBBBBB. B",
            "B.......................... B",
            "B                           B",
            "BBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
        ]
        # fmt: on

        y = 3 * 16
        for row in self.mapa:
            x = 0
            for b in row:
                if b == "B":
                    Cell(x, y, 2)
                elif b == ".":
                    Dot(x + 16, y + 16, 2)
                elif b == "c":
                    Circle(x + 10, y + 10, 2)
                x = x + 16
            y = y + 16


class Cell(EmptyObject):
    def __init__(self, x, y, layer):
        super().__init__(x, y, width=16, height=16, layer=layer, tipo="Bloque")
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
