import tkinter as tk

from MiniGameEngine.GameObject import GameObject


class Text(GameObject):
    """Clase que representa un GameObject definido por un texto."""

    def __init__(
        self,
        x: float,
        y: float,
        layer: int,
        text: str,
        font: str = "Arial 12",
        color: str = "black",
    ):
        """
        Crea una un objeto de la clase Text.

        Args:
            x (float): Coordenada x del texto.
            y (float): Coordenada y del texto.
            layer (int): Capa en que se colocará este texto.
            text (str): Texto para este objeto
            font (str, optional): Font a utilizar para el texto (por defecto es "Arial 12").
            color (str, optional): Color a utilizar para el texto (por defecto es "black").
        """
        super().__init__(x, y, layer=layer, tipo="Text Object")

        gobj = self._getCanvas().create_text(
            self.getX(),
            self.getY(),
            text=text,
            font=font,
            fill=color,
            anchor=tk.NW,
            state="disabled",
            tags=(f"Layer {layer}",),
        )

        self._setElement(gobj)
        self._updateDimension()

    def setText(self, text: str):
        """
        Cambia el texto del objeto.

        Args:
            text (str): El nuevo texto del objeto.
        """
        self._getCanvas().itemconfig(self._getElement(), text=text)
        self._updateDimension()

    def setFont(self, font: str):
        """
        Cambia el Tipo de letra, tamaño y atributo del texto del objeto.
        El nuevo font se puede especificar como "Arial 10 italica bold"

        Args:
            font (str): El nuevo tipo de letra, tamaño y atributo del texto del objeto.
        """
        self._getCanvas().itemconfig(self._getElement(), font=font)
        self._updateDimension()

    def setColor(self, color: str):
        """
        Cambia el color del texto del objeto.

        Args:
            color (str): El nuevo color para el texto del objeto.
        """
        self._getCanvas().itemconfig(self._getElement(), fill=color)

    def _updateDimension(self):
        bbox = self._getCanvas().bbox(self._getElement())
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        self._setDimension(width, height)
