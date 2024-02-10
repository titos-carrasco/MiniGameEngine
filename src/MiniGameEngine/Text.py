import tkinter as tk

from MiniGameEngine.GameWorld import GameWorld
from MiniGameEngine.GameObject import GameObject


class Text(GameObject):
    """
    Clase que representa un GameObject definido por un texto.
    """

    def __init__(
        self,
        x: int,
        y: int,
        layer: int,
        text: str,
        font: str = "Arial",
        size: int = 10,
        bold: bool = False,
        italic: bool = False,
        color: str = "black",
    ):
        """
        Constructor de la clase Text que agrega un Texto al mundo del juego

        Args:
            x (int): Coordenada x del texto
            y (int): Coordenada y del texto
            layer (int): Capa en que se colocará este texto.
            text (str): Texto para este objeto
            font (str, optional): Font a utilizar para el texto (por defecto es "Arial").
            size (int, optional): Tamano a utilizar para el texto (por defecto es 10).
            bold (bool, optional): Especifica que el texto estara en bold (por defecto es False).
            italic (bool, optional): Especifica que el texto estara en italic (por defecto es False).
            color (str, optional): Color a utilizar para el texto (por defecto es "black").
        """
        super().__init__(x, y, layer=layer, tipo="Text Object")

        gobj = self._getCanvas().create_text(
            self.getX(),
            self.getY(),
            text=text,
            anchor=tk.NW,
            state="normal",
            tags=("Layer " + str(self.getLayer()),),
        )

        self._setElement(gobj)
        self.setText(text=text, font=font, size=size, bold=bold, italic=italic, color=color)

    def setText(
        self,
        text: str,
        font: str = None,
        size: int = None,
        bold: bool = None,
        italic: bool = None,
        color: str = None,
    ):
        """
        Modifica el texto desplegado y sus atributos. Si no se especifican atributos se convservan los existentes

        Args:
            text (str): Texto para este objeto
            font (str, optional): Font a utilizar para el texto
            size (int, optional): Tamano a utilizar para el texto
            bold (bool, optional): Especifica que el texto estara en bold
            italic (bool, optional): Especifica que el texto estara en italic
            color (str, optional): Color a utilizar para el texto
        """
        kwargs = {}
        kwargs["text"] = text

        f = []
        if not font is None:
            f.append(font)
        if not size is None:
            f.append(size)
        t = ""
        if bold:
            t = t + " bold "
        if italic:
            t = t + " italic "
        if t:
            f.append(t)
        if f:
            kwargs["font"] = tuple(f)

        if not color is None:
            kwargs["fill"] = color

        self._getCanvas().itemconfig(self._getElement(), kwargs)

        bbox = self._getCanvas().bbox(self._getElement())
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]

        self._setDimension(width, height)
