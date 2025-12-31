from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.EmptyObject import EmptyObject


class Laberinto(Sprite):
    def __init__(self, x, y, layer):
        super().__init__(
            x, y, image_path="./Recursos/Laberinto.png", layer=layer, tipo="Laberinto"
        )

        # fmt: off
        self.mapa = [
                "                             ",
                "                             ",
                "                             ",
                "BBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
                "B             B             B",
                "B             B             B",
                "B  BBB  BBBB  B  BBBB  BBB  B",
                "B  BBB  BBBB  B  BBBB  BBB  B",
                "B                           B",
                "B                           B",
                "B  BBB  B  BBBBBBB  B  BBB  B",
                "B       B     B     B       B",
                "B       B     B     B       B",
                "BBBBBB  BBBB  B  BBBB  BBBBBB",
                "BBBBBB  B           B  BBBBBB",
                "BBBBBB  B           B  BBBBBB",
                "BBBBBB  B  BB   BB  B  BBBBBB",
                "           B     B           ",
                "           B     B           ",
                "BBBBBB  B  BBBBBBB  B  BBBBBB",
                "BBBBBB  B           B  BBBBBB",
                "BBBBBB  B           B  BBBBBB",
                "BBBBBB  B  BBBBBBB  B  BBBBBB",
                "B             B             B",
                "B             B             B",
                "B  BBB  BBBB  B  BBBB  BBB  B",
                "B    B                 B    B",
                "B    B                 B    B",
                "BBB  B  B  BBBBBBB  B  B  BBB",
                "B       B     B     B       B",
                "B       B     B     B       B",
                "B  BBBBBBBBB  B  BBBBBBBBB  B",
                "B                           B",
                "B                           B",
                "BBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
                "                             ",
                "                             "
            ]
        # fmt: on

        y = 0
        for row in self.mapa:
            x = 0
            for b in row:
                if b != " ":
                    Cell(x, y, 100)
                x = x + 16
            y = y + 16


class Cell(EmptyObject):
    def __init__(self, x, y, layer):
        super().__init__(x, y, width=16, height=16, layer=layer, tipo="Bloque")
        self.setCollisionFlag(self.COLLISION_RECEIVER)
