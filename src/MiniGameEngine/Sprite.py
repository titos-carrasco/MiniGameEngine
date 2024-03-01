import tkinter as tk

from MiniGameEngine.GameObject import GameObject


class Sprite(GameObject):
    """Clase que representa un GameObject definido por una imagen."""

    def __init__(self, x: float, y: float, layer: int, tipo: str, image_path: str):
        """
        Crea un objeto de la clase Sprite.

        Args:
            x (float): Coordenada x del sprite.
            y (float): Coordenada y del sprite.
            layer (int): Capa en que se colocará este sprite.
            tipo (str): Tipo de sprite.
            imagePath (str): Archivo con la imagen del sprite.
        """
        super().__init__(x, y, layer=layer, tipo=tipo)

        img = self._getGameWorld().loadImage(image_path)
        gobj = self._getCanvas().create_image(
            self.getX(),
            self.getY(),
            image=img,
            anchor=tk.NW,
            state="disabled",
            tags=(f"Layer {layer:04d}",),
        )
        self._setElement(gobj)
        self._setDimension(img.width(), img.height())

    def setShape(self, image_path: str):
        """
        Cambia la imagen del sprite.

        Args:
            imagePath (str): Archivo con la nueva imagen para el sprite.
        """
        img = self._getGameWorld().loadImage(image_path)
        self._setDimension(img.width(), img.height())
        self._getCanvas().itemconfig(self._getElement(), image=img)
