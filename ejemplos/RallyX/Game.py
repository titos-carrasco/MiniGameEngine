from Car import Car
from Enemy import Enemy

from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.Text import Text
from MiniGameEngine.EmptyObject import EmptyObject


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(
            800,
            576,
            title="Rally X",
            bg_path="Recursos/Fondo.png",
            world_size=(1008, 1536),
            debug="F12",
        )

        # agregamos via programación los muros
        self._addBorders()

        # para mostrar los FPS dentro de la cámara
        self.status_bar = Text(
            10,
            10,
            layer=100,
            tipo="StatusBar",
            text="      fps",
            font=("Courier New", 15, "bold"),
            color="black",
            debug=False,
        )
        self.getCamera().addGameObject(self.status_bar)

        # el heroe
        self.car = Car(436, 1300)
        self.getCamera().setTarget(self.car)

        # los perseguidores
        enemy1 = Enemy(340, 1300, self.getTargetPosition)

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

    def getTargetPosition(self):
        if self.car:
            return self.car.getPosition()
        return None

    # terreno tomado desde https://www.biglist.com/lists/stella/archives/200404/msg00089.html
    def _addBorders(self):
        box = EmptyObject(0, 0, 24 * 5, 24 * 64, 1, "Muro", debug=False)
        box.setCollisionFlag(box.COLLISION_RECEIVER)
        box = EmptyObject(37 * 24, 0, 24 * 5, 24 * 64, 1, "Muro", debug=False)
        box.setCollisionFlag(box.COLLISION_RECEIVER)
        box = EmptyObject(5 * 24, 0, 24 * 32, 24 * 4, 1, "Muro", debug=False)
        box.setCollisionFlag(box.COLLISION_RECEIVER)
        box = EmptyObject(5 * 24, 24 * 60, 24 * 32, 24 * 4, 1, "Muro", debug=False)
        box.setCollisionFlag(box.COLLISION_RECEIVER)

        f = open("Terreno.txt", "r")
        muros = f.readlines()
        f.close()

        row = 4
        for line in muros:
            col = 5
            for c in line:
                if c == "X":
                    box = EmptyObject(
                        col * 24, row * 24, 24, 24, 1, "Muro", debug=False
                    )
                    box.setCollisionFlag(box.COLLISION_RECEIVER)
                col = col + 1
            row = row + 1


# -- show time
game = Game()
game.gameLoop(60)
