import tkinter as tk

from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.GameObject import GameObject


class Sprite(GameObject):
    """
    Clase que representa un GameObject definido por una imagen.
    """

    def __init__(self, x: int, y: int, layer: int, tipo: str, imagePath: str):
        """
        Constructor de la clase Sprite.

        Args:
            x (int): Coordenada x del sprite.
            y (int): Coordenada y del sprite.
            layer (int): Capa en que se colocará este sprite.
            tipo (str): Tipo de sprite.
            imagePath (str): Archivo con la imagen del sprite.
        """
        super().__init__(x, y, layer=layer, tipo=tipo)

        img = self._getGameWorld().loadImage(imagePath)
        shape = self._getCanvas().create_image(
            self.getX(),
            self.getY(),
            image=img,
            anchor=tk.NW,
            state="normal",
            tags=("Layer " + str(self.getLayer()),),
        )
        self._setElement(shape)
        self._setDimension(img.width(), img.height())

    def setShape(self, imagePath: str):
        """
        Cambia la imagen del sprite

        Args:
            imagePath (str): Archivo con la nueva imagen para el sprite
        """
        img = self._getGameWorld().loadImage(imagePath)
        self._setDimension(img.width(), img.height())
        self._getCanvas().itemconfig(self._getElement(), image=img)
